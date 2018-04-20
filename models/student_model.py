import json
from observer import Observable
from models.elective_class import Elective

class StudentModel(Observable):

    def __init__(self, id, elective_class):
        super().__init__()
        self.students = {}
        self.id = id
        self.load_list()
        self.elective_obj = elective_class
        self.elective_list = self.elective_obj.electives

    def load_list(self):
        with open('models/database/user.json', 'r') as f:
            json_str = json.load(f)
            for id, info in json_str.items():
                self.students[id] = info
        self.student = self.students[self.id]

    def save_list(self):
        with open('models/database/user.json', 'w') as f:
            json.dump(self.students,f,indent=4)

    def add_elective(self, elective):
        electives = self.students[self.id]['electives']
        if len(electives) == 0 or (len(electives) == 1 and self.elective_list[electives[0]]['time'] != self.elective_list[elective]['time']):
            if elective not in electives and len(self.elective_list[elective]['students'])<25:
                self.students[self.id]['electives'].append(elective)
                with open('models/database/user.json', 'w') as f:
                    json.dump(self.students, f, indent=4)

                self.notify_all(electives=self.students[self.id]['electives'])
                return True
        return False

    def remove_elective(self, elective):
        if elective in self.students[self.id]['electives']:
            self.students[self.id]['electives'].remove(elective)
            with open('models/database/user.json', 'w') as f:
                json.dump(self.students, f, indent=4)
            self.notify_all(electives=self.students[self.id]['electives'])
            return True
        return False
