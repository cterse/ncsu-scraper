import csv
import json
import os

import requests
from bs4 import BeautifulSoup, Tag

import constants
import ncsu_scrape_methods as nsm
import output
from ncsu_course import NCSUCourse, NCSUCourseSection

# Scrape data from website
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

# Parse the scraped data and get list of courses
html_doc = response.text.replace("\\", "")
soup = BeautifulSoup(html_doc, "html.parser")
course_list = nsm.get_courses_list(soup)

# Ouput the results
output.export_to_json(course_list)
output.export_to_csv(course_list)

print("-------- Total couses: {0}".format(len(course_list)))