from tkinter import *
from models.state_model import StateModel
from controllers.login_controller import LoginController
from models.login_model import LoginModel
from controllers.stu_controller import StudentController
from controllers.admin_controller import AdminController

def main():
    root = Tk()
    state = StateModel()
    LoginController(root, LoginModel(), state)
    StudentController(root, state)
    AdminController(root, state)
    mainloop()

if __name__ == "__main__":
    main()