import requests
import pathlib
import sys

from bs4 import BeautifulSoup
import ncsu_scrape_methods as nsm
sys.path.append(pathlib.Path(__file__).parent.parent.resolve().as_posix())
import constants

def scrape_courses():

	# Scrape data from website
	URL = "https://www.acs.ncsu.edu/php/coursecat/search.php"

	payload = 'course-career=GRAD&course-inequality=%3D&course-number=&current_strm='+ constants.YEAR_CODE_2020 + '' + constants.SEM_CODE_FALL +'&distance-only=0&end-time=&end-time-inequality=%3C%3D&instructor-name=&session=&start-time=&start-time-inequality=%3C%3D&subject=CSC%20-%20Computer%20Science&term=2208'
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
	constants.QUERIED_SEMESTER = constants.SEM_CODE_FALL
	constants.QUERIED_YEAR = constants.YEAR_CODE_2020

	response = requests.request("POST", URL, headers=headers, data = payload)

	# Parse the scraped data and get list of courses
	html_doc = response.text.replace("\\", "")
	soup = BeautifulSoup(html_doc, "html.parser")
	course_list = nsm.get_courses_list(soup)

	# Ouput the results
	import output
	output.export_to_json(course_list)
	output.export_to_csv(course_list)

	print("-------- Total couses: {0}".format(len(course_list)))

scrape_courses()