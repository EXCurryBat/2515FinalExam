from tkinter import *
from models.student_model import StudentModel
from views.admin_view import AdminView
from observer import Observer
from models.elective_class import Elective

class AdminController(Observer):

    def __init__(self, master, state):
        self.master = master
        self.state = state
        self.electives = Elective()
        print(1)
        self.state.add_observer(self)

    def load_model_view(self, id):
        self.view = AdminView(self.master)
        self.model = StudentModel(id, self.electives)
        self.model.add_observer(self)
        self.render_view()

    def render_view(self):
        self.view.admin_id['text'] = self.model.student['id']
        self.view.admin_name['text'] = self.model.student['name']
        self.view.admin_type['text'] = self.model.student['type']
        self.load_elective_list()

    def load_elective_list(self):
        self.view.elective_listbox.delete(0, END)
        for i in self.electives.electives:
            self.view.elective_listbox.insert(END, i)
        self.view.elective_listbox.bind('<<ListboxSelect>>', self.load_student_list)

    def load_student_list(self, e):
        elective = self.view.elective_listbox.get(ACTIVE)
        self.view.student_listbox.delete(0, END)
        for student in self.electives.electives[elective]['students']:
            self.view.student_listbox.insert(END,student)


    def update(self, obj, **kwargs):
        state_alert = kwargs.keys()
        print('admin')
        if 'state' in state_alert:
            if kwargs['state']['type'] == 'admin':
                self.load_model_view(kwargs['state']['id'])
        if 'electives' in state_alert:
            self.render_view()