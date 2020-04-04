from bs4 import BeautifulSoup
import requests
import ncsu_scrape_methods as nsm
import unittest

class TestNCSUScrapeMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
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
        print("Successfully scraped HTML.")

        self.soup = BeautifulSoup(html_doc, "html.parser")

    def test_get_section_component_col_index(self):
        table = self.soup.find("section", class_="course").find("table", class_="section-table")
        
        self.assertEqual(nsm.get_section_component_column_index(table, "avail."), 3)
        self.assertIsNone(nsm.get_section_component_column_index(table, "random"))

if __name__ == "__main__":
    unittest.main()