from tkinter import *
import os
from observer import Observer
from tkinter import messagebox
from views.student_view import StudentView
from models.student_model import StudentModel
from models.elective_class import Elective


class StudentController(Observer):

    def __init__(self, master, state):
        self.master = master
        self.state = state
        self.electives = Elective()
        self.state.add_observer(self)

    def load_model_view(self, id):
        self.view = StudentView(self.master)
        self.model = StudentModel(id, self.electives)
        self.model.add_observer(self)
        self.render_view()

    def render_view(self):
        self.view.stu_id['text'] = self.model.student['id']
        self.view.stu_name['text'] = self.model.student['name']
        self.view.stu_type['text'] = self.model.student['type']
        self.view.stu_term['text'] = self.model.student['term']

        self.view.add_button.configure(command=self.add_elective)
        self.view.delete_button.configure(command=self.delete_elective)
        self.view.elec_option_listbox.bind('<<ListboxSelect>>', self.show_description)
        self.load_electivebox()
        self.load_elec_options()

    def show_description(self, e):
        selection = self.view.elec_option_listbox.get(ACTIVE)
        messagebox.showinfo(title=self.electives.electives[selection]['name'], message= self.electives.electives[selection]['description'])
        # self.view.elective_name['text'] = self.electives.electives[selection]['name']
        # self.view.elective_description['text'] = self.electives.electives[selection]['description']

    def load_electivebox(self):
        electives = self.model.student['electives']
        self.view.elective_listbox.delete(0, END)
        for i in electives:
            self.view.elective_listbox.insert(END, i)

    def load_elec_options(self):
        self.view.elec_option_listbox.delete(0, END)
        for elective in self.electives.electives:
            self.view.elec_option_listbox.insert(END,elective)

    def add_elective(self):
        new_elective = self.view.elec_option_listbox.get(ACTIVE)
        if self.model.add_elective(new_elective):
            self.electives.add_student_to_elec(new_elective, self.model.id)

    def delete_elective(self):
        sel_elective = self.view.elective_listbox.get(ACTIVE)
        if self.model.remove_elective(sel_elective):
            self.electives.remove_student(sel_elective, self.model.id)

    def update(self, obj, **kwargs):
        state_alert = kwargs.keys()
        print(state_alert)
        if 'state' in state_alert:
            if kwargs['state']['type'] == 'student':
                self.load_model_view(kwargs['state']['id'])
        if 'electives' in state_alert:
            self.render_view()









