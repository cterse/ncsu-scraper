class Course():
    def __init__(self):
        self.name = None
        self.id = None
        self.credits = None
        self.description = None
        self.semsters = None
        self.course_sections = None

class CourseSection():
    def __init__(self):
        self.section = None
        self.component = None
        self.class_number = None
        self.total_seats = None
        self.available_seats = None
        self.course_section_status = None
        self.location = None
        self.instructor = None
        self.begin_date = None
        self.end_date = None