from tkinter import *

class AdminView():

    def __init__(self, master):
        self.master = master
        self.pack()

    def pack(self):
        # frame container
        self.sub = Frame(self.master)
        self.sub.pack()

        # frames

        self.top_frame = Frame(self.sub)
        self.mid_frame = Frame(self.sub)
        self.bot_frame = Frame(self.sub)
        self.right_frame = Frame(self.sub)

        self.top_frame.grid(row=0, column=0, padx=30, pady=10)
        self.mid_frame.grid(row=1, column=0, padx=30, pady=10)
        self.bot_frame.grid(row=2, column=0, padx=30, pady=10)
        self.right_frame.grid(row=0, column=1, rowspan=2, padx=30, pady=10)

        # widgets
        self.admin_id = Label(self.top_frame, text='')
        self.admin_name = Label(self.top_frame, text='')
        self.admin_type = Label(self.top_frame, text='')

        self.admin_id.grid(row=0,column=0)
        self.admin_name.grid(row=1,column=0)
        self.admin_type.grid(row=2,column=0)

        self.electives = Label(self.mid_frame, text='Electives: ')
        self.elective_listbox = Listbox(self.mid_frame, width=20, selectmode=SINGLE)
        self.elective_scrollbar = Scrollbar(self.mid_frame, orient='vertical')
        self.elective_scrollbar.config(command=self.elective_listbox.yview)
        self.elective_listbox.config(yscrollcommand=self.elective_scrollbar.set)
        self.electives.pack()
        self.elective_listbox.pack(side=LEFT, fill=BOTH)
        self.elective_scrollbar.pack(side=RIGHT, fill=Y)

        self.student_list_label = Label(self.right_frame, text='Current students: ')
        self.student_listbox = Listbox(self.right_frame, width=20, selectmode=SINGLE)
        self.student_scrollbar = Scrollbar(self.right_frame, orient='vertical')
        self.student_scrollbar.config(command=self.student_listbox.yview)
        self.student_listbox.config(yscrollcommand=self.student_scrollbar.set)
        self.student_list_label.pack()
        self.student_listbox.pack(side=LEFT, fill=BOTH)
        self.student_scrollbar.pack(side=RIGHT, fill=Y)


    def unpack(self):
        self.sub.pack_forget()