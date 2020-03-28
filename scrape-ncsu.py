import json
from ncsu_course import Course, CourseSection
from bs4 import BeautifulSoup
from bs4 import Tag
import requests
import ncsu_scrape_methods as nsm

url = "https://www.acs.ncsu.edu/php/coursecat/search.php"

payload = 'course-career=GRAD&course-inequality=%3D&course-number=&current_strm=2208&distance-only=0&end-time=&end-time-inequality=%3C%3D&instructor-name=&session=&start-time=&start-time-inequality=%3C%3D&subject=CSC%20-%20Computer%20Science&term=2208'
headers = {
	'Origin': 'https://www.acs.ncsu.edu',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Sec-Fetch-Dest': 'empty',
	'X-Requested-With': 'XMLHttpRequest',
	'DNT': '1',
	'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)
html_doc = response.text.replace("\\", "")

soup = BeautifulSoup(html_doc, "html.parser")

course_list = []

course_sections = soup.findAll("section", class_="course")
for section in course_sections:
	course_id = nsm.get_course_id(section)
	if not course_id: continue

	course = Course()
	course.id = course_id
	course.name = nsm.get_course_name(section)
	course.credits = nsm.get_course_credits_tuple(section)
	course.course_sections = nsm.get_course_sections_list(section)
	
	course_list.append(course)

op_file = open("./op.json", "w")
for course in course_list:
	op_file.write(str(course))

print("-------- Total couses: {0}".format(len(course_list)))