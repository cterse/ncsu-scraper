'''
Data output utils.
'''

import csv
import os
import sys
import pathlib
from typing import Any, List, Optional
import logging

from ncsu_course import NCSUCourse
# sys.path.append(pathlib.Path(__file__).parent.parent.resolve().as_posix())
import constants

log = logging.getLogger("default_logger")

# Output constants
OUTPUT_FOLDER_NAME = "output"
OUTPUT_FILE_NAME_PREFIX = "ncsu_courses"

def create_output_directory(dir_name: str = OUTPUT_FOLDER_NAME) -> Optional[str]: 
    op_folder_path = os.path.join(constants.ROOT_DIR, dir_name)
    try:
        os.mkdir(op_folder_path)
        log.info("Output directory created.")
        return op_folder_path
    except FileExistsError:
        log.info("Output directory already present.")
        return op_folder_path
    except:
        log.info("Error creating output directory.")
        return None

def get_output_filename(filetype: str) -> Optional[str]:
	if not filetype: return None

	return OUTPUT_FILE_NAME_PREFIX + "_" + constants.QUERIED_YEAR + "" + constants.QUERIED_SEMESTER + "." + filetype

def export_to_json(courses: List[NCSUCourse]) -> int:
	if not courses: return -1

	op_folder_path = create_output_directory(OUTPUT_FOLDER_NAME)

	try:
		output_file = os.path.join(op_folder_path, get_output_filename("json"))
		op_file = open(output_file, "w")
		for course in courses:
			op_file.write(str(course))
	except:
		return -1

	return 0

def export_to_csv(courses: List[NCSUCourse]) -> int:
	if not courses: return -1

	op_folder_path = create_output_directory(OUTPUT_FOLDER_NAME)

	try:
		output_file = os.path.join(op_folder_path, get_output_filename("csv"))
		with open(output_file, "w", newline="") as file:
			writer = csv.writer(file)
			writer.writerow(["Course ID", "Course Name", "Course Status", "Course Prerequisites", "Section", "Available Seats", "Total Seats", "Section Status", "Instructor", "Min credits", "Max credits"])

			csv_course_list: List[List[Any]] = []
			for course in courses:
				for course_section in course.course_sections:
					temp_list: List[Any] = []

					temp_list.append(course.id)
					temp_list.append(course.name)
					temp_list.append(course.get_course_status())
					temp_list.append(course.course_prereq)
					temp_list.append(course_section.section)
					temp_list.append(course_section.available_seats)
					temp_list.append(course_section.total_seats)
					temp_list.append(course_section.section_status)
					temp_list.append(course_section.instructor)
					temp_list.append(course.credits[0])
					temp_list.append(course.credits[1])

					csv_course_list.append(temp_list)

			writer.writerows(csv_course_list)
			return 0
	except Exception as e:
		log.error(e)
		return -1
