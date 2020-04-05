from typing import List, Optional, Tuple

# NCSU Course Constants
NCSU_COURSE_STATUS_OPEN = "OPEN"
NCSU_COURSE_STATUS_CLOSED = "CLOSED"
NCSU_COURSE_STATUS_WAITLIST = "WAITLIST"
NCSU_COURSE_STATUS_RESERVED = "RESERVED"

class NCSUCourse():
    def __init__(self):
        self.name: Optional[str] = None
        self.id: str = None
        self.credits: Tuple(int, int) = None
        self.description: str = None
        self.semsters: List[str] = None
        self.course_sections: List[NCSUCourseSection] = None
        self.course_status: str = None
        self.course_prereq: str = None

    def get_course_status(self) -> Optional[str]:
        if not self.course_sections: return None

        section_status_set = set([section.section_status.upper() for section in self.course_sections])
        
        if len(section_status_set) == 1: return section_status_set.pop()
        elif NCSU_COURSE_STATUS_OPEN in section_status_set: return NCSU_COURSE_STATUS_OPEN
        elif NCSU_COURSE_STATUS_RESERVED in section_status_set: return NCSU_COURSE_STATUS_RESERVED
        elif NCSU_COURSE_STATUS_WAITLIST in section_status_set: return NCSU_COURSE_STATUS_WAITLIST
        else: return NCSU_COURSE_STATUS_CLOSED

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

class NCSUCourseSection():
    def __init__(self):
        self.section: int = None
        self.component: str = None
        self.class_number: str = None
        self.total_seats: int = None
        self.available_seats: int = None
        self.section_status: str = None
        self.location: str = None
        self.instructor: str = None
        self.begin_date: str = None
        self.end_date: str = None

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)
