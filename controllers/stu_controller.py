from tkinter import *
import os
from observer import Observer
from views.student_view import StudentView
from models.student_model import StudentModel


class StudentController(Observer):

    def __init__(self, master, state):
        self.master = master
        self.model = StudentModel
        self.state = state

        self.state.add_observer(self)

    def load_model_view(self):
        self.view = StudentView(self.master)

    def update(self, obj, **kwargs):
        state_alert = kwargs.keys()
        if kwargs['state']['type'] == 'student':
            self.object = kwargs['state']
            self.load_model_view()










