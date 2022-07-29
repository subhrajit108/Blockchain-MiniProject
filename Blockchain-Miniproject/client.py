from tkinter import *
from tkinter import ttk
import json

class Form:
	counter=0
	def __init__(self, window, master):
		window.title("VANET Blockchain Login System")
		window.geometry('400x400')
		car_reg_no_text = Label(window ,text = "Car Registration Number").grid(row = 0,column = 0) 
		license_no_text = Label(window ,text = "License Number").grid(row = 1,column = 0) 
		owner_name_text= Label(window ,text = "Owner Name").grid(row = 2,column = 0) 
		pseudonym_text = Label(window ,text = "Pseudonym").grid(row = 3,column = 0) 

		car_reg_no=StringVar()
		license_no=StringVar()
		owner_name=StringVar()
		pseudonym=StringVar()

		car_reg_no_entry = Entry(window, textvariable=car_reg_no).grid(row = 0,column = 1)
		license_no_entry = Entry(window, textvariable=license_no).grid(row = 1,column = 1)
		owner_name_entry = Entry(window, textvariable=owner_name).grid(row = 2,column = 1)
		pseudonym_entry = Entry(window, textvariable=pseudonym).grid(row = 3,column = 1)

		self.car_reg_no=car_reg_no
		self.license_no=license_no
		self.owner_name=owner_name
		self.pseudonym=pseudonym

		btn1 = ttk.Button(window ,text="Submit", command = lambda:self.save_info(window, master)).grid(row=4,column=0)
		btn2 = ttk.Button(window ,text="Exit", command = lambda:self.exit(window, master)).grid(row=4,column=1)

	def save_info(self, window, master):
		car_reg_no_info=self.car_reg_no.get()
		license_no_info=self.license_no.get()
		owner_name_info=self.owner_name.get()
		pseudonym_info=self.pseudonym.get()
		Form.counter+=1
		file = open("vehicle_information.txt", "a+")
		file.write("Transaction No: "+str(Form.counter)+", ")
		file.write("Car Registration Number: " + car_reg_no_info + ", ")
		file.write("License Number: "+ license_no_info + ", ")
		file.write("Car Owner Name: " + owner_name_info + ", ")
		file.write("Pseudonym: " + pseudonym_info + "\n")
		file.close()
		print("SUBMITTED")
		window.withdraw()
		self.car_reg_no.set('')
		self.license_no.set('')
		self.owner_name.set('')
		self.pseudonym.set('')
		# master.deiconify()
		choose=Toplevel(window)
		choose.title("Please Choose")
		choose.geometry('350x100')
		l = Label(choose, text = "Thank you for submitting.")
		btn1 = ttk.Button(choose ,text="Submit another car information record", width=50, command=lambda:self.option(1, choose, window, master)).grid(row=0,column=0, pady=10, padx=10)
		btn2 = ttk.Button(choose ,text="Go back to login page", width=50, command=lambda:self.option(2, choose, window,master)).grid(row=1,column=0)

	def option(self, btn, choose, master, root):
		choose.destroy()
		if(btn==1):
			master.deiconify()
		if(btn==2):
			master.destroy()
			root.deiconify()

	def exit(self, window, master):
		window.destroy()
		master.deiconify()


