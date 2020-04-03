from ncsu_course import NCSUCourse
from ncsu_course import NCSUCourseSection
from typing import Tuple
from typing import List
from typing import Optional
from bs4 import Tag
from bs4 import NavigableString
from bs4 import BeautifulSoup

def get_courses_list(soup: BeautifulSoup) -> List[NCSUCourse]:
	if not soup: return []

	course_list = []
	course_sections = soup.findAll("section", class_="course")
	for section in course_sections:
		course_id = get_course_id(section)
		if not course_id: continue

		course = NCSUCourse()
		course.id = course_id
		course.name = get_course_name(section)
		course.credits = get_course_credits_tuple(section)
		course.course_sections = get_course_sections_list(section)
		
		course_list.append(course)
	
	return course_list

def get_course_id(section: Tag) -> Optional[str]:
	if not section: return None
	if not section.h1 or not section.h1.contents: return None
	return section.h1.contents[0].strip()

def get_course_name(section: Tag) -> Optional[str]:
	if not section: return None
	if not section.h1 or not section.h1.contents: return None

	return section.h1.small.string.strip()

def get_course_credits_tuple(section: Tag) -> Optional[Tuple[int, int]]:
    if not section: return None
    if not section.h1 or not section.h1.contents: return None

    credits_range_arr = section.h1.span.string.split(":")[1].split("-")
    if not credits_range_arr: return None
    
    min_creds = int(credits_range_arr[0].strip())
    if len(credits_range_arr) == 1: max_creds = min_creds
    else: max_creds = int(credits_range_arr[1].strip())

    return (min_creds, max_creds)

def get_course_sections_list(section: Tag) -> List[NCSUCourseSection]:
	if not section: return []
	section_table = section.find("table", class_="section-table")
	if not section_table or not section_table.tr: return []

	course_section_list = []
	for child in section_table.children:
		if child.name != "tr": continue
		row = child
		if not row.contents: continue
		course_section = NCSUCourseSection()
		course_section.section = row.contents[0].string.strip() if row.contents[0].string else None
		course_section.component = row.contents[1].string.strip() if len(row.contents) > 1 and row.contents[1].string else None
		course_section.class_number = row.contents[2].string.strip() if len(row.contents) > 2 and row.contents[2].string else None
		course_section.location = row.contents[5].string.strip() if len(row.contents) > 5 and row.contents[5].string else None
		course_section.instructor = row.contents[6].a.string.strip() if len(row.contents) > 6 and row.contents[6].a else row.contents[6].string.strip()
		course_section.begin_date = row.contents[7].string.split("-")[0].strip() if len(row.contents) > 7 and row.contents[7].string else None
		course_section.end_date = row.contents[7].string.split("-")[1].strip() if len(row.contents) > 7 and row.contents[7].string and len(row.contents[7].string.split("-")) > 1 else None
		course_section.section_status = row.contents[3].span.string.strip().upper() if len(row.contents) > 3 and row.contents[3].span and row.contents[3].span.string else None
		course_section.available_seats = row.contents[3].contents[2].string.split("/")[0].strip() if len(row.contents) > 3 and row.contents[3].contents and len(row.contents[3].contents) > 2 and row.contents[3].contents[2].string else None
		if course_section.section_status and course_section.section_status.lower() == "waitlist":
			course_section.total_seats = row.contents[3].contents[2].string.split("/")[1].strip().split(" ")[0] if len(row.contents) > 3 and row.contents[3].contents and len(row.contents[3].contents) >2 and row.contents[3].contents[2].string and len(row.contents[3].contents[2].string.split("/")) > 1 else None
		else:
			course_section.total_seats = row.contents[3].contents[2].string.split("/")[1].strip() if len(row.contents) > 3 and row.contents[3].contents and len(row.contents[3].contents) >2 and row.contents[3].contents[2].string and len(row.contents[3].contents[2].string.split("/")) > 1 else None

		course_section_list.append(course_section)
	
	return course_section_list

def get_section_component_column_index(table: Tag, section_component: str) -> int:
	if not table or not section_component: return -1

	col_index = -1
	col_header_row = table.thead.tr
	for i in range(0, len(col_header_row.contents)):
		if col_header_row.contents[i].string: 
			if col_header_row.contents[i].string.lower() == section_component.lower():
				col_index = i
				break
		else:
			for child in col_header_row.contents[i].contents:
				if isinstance(child, NavigableString):
					if child.string.lower() == section_component.lower():
						col_index = i
						break
	
	return col_index if col_index > -1 else -1

def get_section_component_tag(table: Tag, section_component: str) -> Tag:
	if not table or not section_component: return None

	col_index = get_section_component_column_index(table, section_component)
	if col_index is None: return None

	sec_val_dict = {}
	for child in table.children:
		if child.name != "tr": continue
		row = child
		if not row.contents: continue

		sec_id = row.contents[0].string.strip()
		sec_value = row.contents[col_index]

		sec_val_dict[sec_id] = sec_value
	
	return sec_val_dict