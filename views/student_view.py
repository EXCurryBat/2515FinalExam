from tkinter import *

class StudentView():

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
        self.bot_right_frame = Frame(self.sub)
        self.description_frame = Frame(self.sub)

        self.top_frame.grid(row=0,column=0, padx=30, pady=10)
        self.mid_frame.grid(row=1,column=0, padx=30, pady=10)
        self.bot_frame.grid(row=2,column=0, padx=30, pady=10)
        self.right_frame.grid(row=0,column=1,rowspan=2, padx=30,pady=10)
        self.bot_right_frame.grid(row=3, column=1,padx=30,pady=10)
        self.description_frame.grid(row=0, column=2,rowspan=3, padx=30, pady=10)

        # widgets
        self.stu_id = Label(self.top_frame, text='')
        self.stu_name = Label(self.top_frame, text='')
        self.stu_type = Label(self.top_frame, text='')
        self.stu_term = Label(self.top_frame, text='')
        self.stu_id.grid(row=0,column=0)
        self.stu_name.grid(row=0,column=1)
        self.stu_type.grid(row=1,column=0)
        self.stu_term.grid(row=1,column=1)

        self.electives = Label(self.mid_frame, text='Electives: ')
        self.elective_listbox = Listbox(self.mid_frame, width=20, selectmode=SINGLE)
        self.elective_scrollbar = Scrollbar(self.mid_frame, orient='vertical')
        self.elective_scrollbar.config(command=self.elective_listbox.yview)
        self.elective_listbox.config(yscrollcommand=self.elective_scrollbar.set)
        self.electives.pack()
        self.elective_listbox.pack(side = LEFT,fill=BOTH)
        self.elective_scrollbar.pack(side=RIGHT, fill=Y)

        self.delete_button = Button(self.bot_frame, text='delete', width=10)
        self.delete_button.pack()

        self.elec_option_text = Label(self.right_frame, text='Available electives: ')
        self.elec_option_listbox = Listbox(self.right_frame, width=20, selectmode=SINGLE)
        self.elec_option_scrollbar = Scrollbar(self.right_frame, orient='vertical')
        self.elec_option_scrollbar.config(command=self.elec_option_listbox.yview)
        self.elec_option_listbox.config(yscrollcommand=self.elec_option_scrollbar.set)
        self.elec_option_text.pack()
        self.elec_option_listbox.pack(side=LEFT, fill=BOTH)
        self.elec_option_scrollbar.pack(side=RIGHT, fill=Y)

        self.add_button = Button(self.bot_right_frame, text='Add', width=10)
        self.add_button.pack()

        # self.elective_name = Label(self.description_frame, text='', width=30)
        # self.elective_description = Label(self.description_frame, text='', width=30)
        # self.elective_name.grid(row=0, padx=30, pady=10)
        # self.elective_description.grid(row=1, rowspan=2, padx=30, pady=10)


    def unpack(self):
        self.sub.pack_forget()