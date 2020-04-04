'''
Data output utils.
'''

import csv
import os
import sys
import pathlib
from typing import Any, List

from ncsu_course import NCSUCourse
sys.path.append(pathlib.Path(__file__).parent.parent.resolve().as_posix())
import constants

# Output constants
OUTPUT_FOLDER_NAME = "output"
OUTPUT_FILE_NAME = "ncsu_courses"

def create_output_directory(dir_name: str = OUTPUT_FOLDER_NAME) -> int: 
    op_folder_path = os.path.join(constants.ROOT_DIR, dir_name)
    try:
        os.mkdir(op_folder_path)
        print("Output directory created.")
        return 0
    except FileExistsError:
        print("Output directory already present.")
        return 0
    except:
        print("Error creating output directory.")
        return 1

def export_to_json(courses: List[NCSUCourse]) -> int:
	if not courses: return -1

	create_output_directory(OUTPUT_FOLDER_NAME)

	try:
		output_file = os.path.join(OUTPUT_FOLDER_PATH, OUTPUT_FILE_NAME+".json")
		op_file = open(output_file, "w")
		for course in courses:
			op_file.write(str(course))
	except:
		return -1

	return 0

def export_to_csv(courses: List[NCSUCourse]) -> int:
	if not courses: return -1

	create_output_directory(OUTPUT_FOLDER_NAME)

	try:
		output_file = os.path.join(OUTPUT_FOLDER_PATH, OUTPUT_FILE_NAME+".csv")
		with open(output_file, "w", newline="") as file:
			writer = csv.writer(file)
			writer.writerow(["Course ID", "Course Name", "Course Status", "Section", "Available Seats", "Total Seats", "Section Status", "Instructor", "Min credits", "Max credits"])

			csv_course_list: List[List[Any]] = []
			for course in courses:
				for course_section in course.course_sections:
					temp_list: List[Any] = []

					temp_list.append(course.id)
					temp_list.append(course.name)
					temp_list.append(course.get_course_status())
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
	except:
		return -1
