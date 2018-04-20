import json

class Elective():

    def __init__(self):
        self.electives = {}
        self.load()

    def load(self):
        with open('models/database/electives.json', 'r') as f:
            json_str = json.load(f)
            for course_id, info in json_str.items():
                self.electives[course_id] = info

    def save(self):
        with open('models/database/electives.json', 'w') as f:
            json.dump(self.electives, f, indent=4)

    def add_student_to_elec(self, elective, id):
        student_list = self.electives[elective]['students']
        if id not in student_list and len(student_list) < 25:
            self.electives[elective]['students'].append(id)
        self.save()

    def remove_student(self, elective, id):
        student_list = self.electives[elective]['students']
        if id in student_list:
            self.electives[elective]['students'].remove(id)
        self.save()