from typing import Tuple
from bs4 import Tag

def get_ncsu_course_id(section: Tag) -> str:
	if not section.h1 or not section.h1.contents: return None

	return section.h1.contents[0].strip()

def get_ncsu_course_name(section: Tag) -> str:
	if not section.h1 or not section.h1.contents: return None

	return section.h1.small.string.strip()

def get_ncsu_course_credits_tuple(section: Tag) -> Tuple[int, int]:
    if not section.h1 or not section.h1.contents: return None

    credits_range_arr = section.h1.span.string.split(":")[1].split("-")
    if not credits_range_arr: return None
    
    min_creds = int(credits_range_arr[0].strip())
    if len(credits_range_arr) == 1: max_creds = min_creds
    else: max_creds = int(credits_range_arr[1].strip())

    return (min_creds, max_creds)
