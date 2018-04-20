from tkinter import *
import os
from observer import Observer
from views.login_view import LoginView


class LoginController(Observer):

    def __init__(self, master, login, state):
        self.master = master
        self.model = login
        self.view = LoginView(master)
        self.state = state

        self.state.add_observer(self)


        self.view.file_menu.add_command(label='Quit', command=self.master.quit)
        self.view.login_but.config(command=self.login_ver)

    def login_ver(self):
        id = self.view.id_entry.get()
        password = self.view.pw_entry.get()
        if id != '' and password != '':
            self.log_response = self.model.verify_user(id, password)
            if self.log_response != False:
                self.state.state = self.log_response

    def update(self, obj, **kwargs):
        state_alert = kwargs.keys()
        if 'state' in state_alert:
            if kwargs['state'] != '':
                self.view.unpack()
            if kwargs['state'] == '':
                self.view.pack()









