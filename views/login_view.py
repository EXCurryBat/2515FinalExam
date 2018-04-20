from tkinter import *

class LoginView:

    def __init__(self, master):
        self.master = master
        self.master.title('Elective management login window')
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.pack()

    def pack(self):


        # frame container

        self.sub = Frame(self.master)
        self.sub.pack()

        # frames

        self.top_frame = Frame(self.sub)
        self.mid_frame = Frame(self.sub)
        self.bot_frame = Frame(self.sub)

        self.top_frame.grid(row=0, padx=30, pady=10)
        self.mid_frame.grid(row=1, padx=30, pady=10)
        self.bot_frame.grid(row=2, padx=30, pady=10)

        #widgets

        self.top_label = Label(self.top_frame, text="Welcome to elective management")
        self.id_label = Label(self.mid_frame, text="Enter ID")
        self.id_entry = Entry(self.mid_frame, font=(35), justify=CENTER)
        self.pw_entry = Entry(self.mid_frame, font=(35), justify=CENTER)
        self.pw_label = Label(self.mid_frame, text="Enter password")
        self.login_msg = Label(self.mid_frame, text="")

        self.top_label.grid(row=0)
        self.id_label.grid(row=0)
        self.id_entry.grid(row=1)
        self.pw_label.grid(row=2)
        self.pw_entry.grid(row=3)
        self.login_msg.grid(row=4)

        self.login_but = Button(self.bot_frame, text='Login')
        self.login_but.grid(row=0)

    def unpack(self):
        self.sub.pack_forget()

if __name__ == "__main__":
    root = Tk()
    view = LoginView(root)
    mainloop()