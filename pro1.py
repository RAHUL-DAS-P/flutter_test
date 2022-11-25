from tkinter import *
import mysql.connector as con
from PIL import Image,ImageTk
import csv
list_id=[]
list_pw=[]
d = {}
db = con.connect(host="localhost",username="root",passwd="rahul783810072003",database  = "mypy")
c = db.cursor()
w = Tk()		
w.title('student registration system')
w.geometry('1400x700+0+0')

# c.execute('''CREATE TABLE student(
# 	NAME varchar(30),
#  	ROLLNO int PRIMARY KEY AUTO_INCREMENT,
#  	MARKS int,
#  	DOB date NOT NULL,
#  	CLASS char(3,)
#  	STREAM varchar(30));''')



nolabel = Label(w)


'''
with open('student_registration_system.csv','w',newline='') as f:
		rdr=csv.writer(f)
		rdr.writerow(['stu_code','password', 'stu_name', 'stu_class', 'stu_sec', 'stu_DOB'])
'''

with open('student_registration_system.csv','r') as f:
		rdr=csv.reader(f)
		for line in rdr:
			if line[0] == 'stu_code':
				continue
			else:
				list_pw=list_pw+[line[1]]
				list_id=list_id+[line[0]]
				d[line[0]] = [line[1],line[2],line[3],line[4],line[5]]
			#print(line)


def loginpage():
	top1 = Toplevel()
	top1.geometry("1400x700+0+0")

			



def addingelementsincsv(a,b,c,d,e,g):
	global cid
	global cpw
	with open('student_registration_system.csv','a',newline='') as f:
		wtr=csv.writer(f)
		wtr.writerow([a,b,c,d,e,g])





def login():
	global w
	global nolabel
	global list_id
	global list_pw
	givenid = identry.get()
	givenpw = pwentry.get()
	try:
		if givenid in list_id and givenpw in list_pw:
			nolabel.destroy()
			loginpage()
			

		else:
			nolabel.destroy()

			nolabel = Label(frame2,text='incorrect password/ID',fg='red')
			nolabel.place(x=500,y=400)
	except Exception:
			nolabel.destroy()
			nolabel = Label(frame2,text='try logging in again',fg='#FFD433')
			nolabel.grid(row=5,column=1)

	identry.delete(0,END)
	pwentry.delete(0,END)

def cancel(window):
	window.destroy()


def submit():
	global list_pw
	global list_id
	cid = cidentry.get()
	cpw = cpwentry.get()
	cname=csnameentry.get()
	cclass = cclassentry.get()
	csec = csecentry.get()
	cdob = cdobentry.get()
	if (len(cid) and len(cpw)) ==0:
			l = Label(top2,text='enter valid password/ID',fg='red')
			l.grid(row=9,column=1,columnspan=2)

			
	else:
			if cid not in list_id and cpw not in list_pw:
				l = Label(top2,text='                                                           ')
				l.grid(row=9,column=1,columnspan=2)
				list_id.append(cid)
				list_pw.append(cpw)
				l1 = Label(top2,text='account created',fg='green')
				l1.grid(row=9,column=1,columnspan=2)
				addingelementsincsv(cid,cpw,cname,cclass,csec,cdob)
			else:
				l = Label(top2,text='password/ID already exist',fg='#FE1F4B')
				l.grid(row=9,column=1,columnspan=2)
	cidentry.delete(0,END)
	cpwentry.delete(0,END)
	csnameentry.delete(0,END)
	cclassentry.delete(0,END)
	csecentry.delete(0,END)
	cdobentry.delete(0,END)



def create_account():
	global cid
	global cpw
	global top2
	global cidentry
	global cpwentry
	global csnameentry
	global cclassentry
	global csecentry
	global cdobentry

	

	top2 = Toplevel()
	cl = Label(top2,text='provide details here')
	cidlabel = Label(top2,text='USERNAME/UNICODE')
	cpwlabel = Label(top2,text='PASSWORD')
	#cuid = Label(top2,text='STU_CODE')
	csnamelabel = Label(top2,text='STUDENT_NAME')
	cclasslabel = Label(top2,text='CLASS')
	cseclabel = Label(top2,text='SECTION')
	cdoblabel = Label(top2,text='DOB')




	cidentry = Entry(top2,width=30,borderwidth=3,)
	cpwentry = Entry(top2,width=30,borderwidth=3)
	#cuidentry = Entry(top2,width=30,borderwidth=3)
	csnameentry = Entry(top2,width=30,borderwidth=3)
	cclassentry = Entry(top2,width=30,borderwidth=3)
	csecentry = Entry(top2,width=30,borderwidth=3)
	cdobentry = Entry(top2,width=30,borderwidth=3)

	csubbtn = Button(top2,text='OK SUBMIT',command=submit,padx=155,pady=5)
	cblank = Label(top2,text='')
	close = Button(top2,text='click to close',command=lambda:cancel(top2),padx=64,pady=3)


	cl.grid(row=0,column=0,columnspan=2)
	cidlabel.grid(row=2,column=0)
	cpwlabel.grid(row=3,column=0)

	csnamelabel.grid(row=4,column=0)
	cclasslabel.grid(row=5,column=0)
	cseclabel.grid(row=6,column=0)
	cdoblabel.grid(row=7,column=0)


	cidentry.grid(row=2,column=1)
	cpwentry.grid(row=3,column=1)
	csnameentry.grid(row=4,column=1)
	cclassentry.grid(row=5,column=1)
	csecentry.grid(row=6,column=1)
	cdobentry.grid(row=7,column=1)
	csubbtn.grid(row=8,column=0,columnspan=2)
	cblank.grid(row=9,column=0)
	close.grid(row=10,column=1,columnspan=1)
	
	
	
	






frame1 = Frame(w,bg = 'white').place(x=0,y=0,width = 200,height = 700)
frame2 = Frame(w).place(x=200,y=0,height = 700)


imagekvs = ImageTk.PhotoImage(file='bk.png')
imagelabels = Label(w,image=imagekvs)
imagelabels.place(x=200,y=0,relwidth = 1,relheight = 1)

title = Label(w ,text = 'Student Login System',font = ("Times",30,'bold'),bg= 'black',fg= 'yellow').place(x=0,width = 1400,height = 50)

frame3 = Frame(w).place(x=100,y=100,width = 1200,height = 500)
imagekvsd = ImageTk.PhotoImage(file='a.jpg')
imagelabelsd = Label(frame3,image=imagekvsd,width = 200,bd=2)
imagelabelsd.place(x=110,y=200)

# imagelogin = ImageTk.PhotoImage(file='login1.jpg')


crlabel = Label(frame2,text="'If you don not have an account ...try creating one...Click 'CREATE ACCOUNT'",font = ("Lucida",13,'bold'),fg='green')
login_header = Label(frame2,text='LOGIN PAGE',font = ("Times",20,'bold'))
idlabel = Label(frame2,text='STUDENT_ID',font = ("Times",15,'bold'))
pwlabel = Label(frame2,text='STUDENT_PASSWORD',font = ("Times",15,'bold'))
identry = Entry(frame2,width=30,borderwidth=3,font = ("Lucida",15,'bold'))
pwentry = Entry(frame2,width=30,borderwidth=3,font = ("Lucida",15,'bold'))
loginbtn = Button(frame2,bg='#FF3F33',command=login,text="LOGIN",font=("Times",20,'bold'))
loginbtn["borderwidth"]=5
blank = Label(frame2,text='')
crac = Button(frame2,text='CREATE ACCOUNT',font = ("Times",17,'bold'),command=create_account,bg='#6AFF33',relief = "groove",bd=5)
showdatabtn = Button(frame2,text='show data',font = ("Times",20,'bold'),command=login,padx=64,pady=3)




# login_header.grid(row=180,column=149,columnspan=2)
# idlabel.grid(row=181,column=149)
# pwlabel.grid(row=182,column=149)
# identry.grid(row=181,column=150)
# pwentry.grid(row=182,column=150)
# loginbtn.grid(row=183,column=149,columnspan=2,ipadx=30)
# blank.grid(row=184,column=143)
# crac.grid(row=185,column=150,columnspan=1)
# showdatabtn.grid(row=185,column=149,columnspan=1)



login_header.place(x=700,y=150)
idlabel.place(x=400,y=250)
pwlabel.place(x=400,y=300)
identry.place(x=700,y=250)
pwentry.place(x=700,y=300)
loginbtn.place(x=500,y=350,relwidth=0.32,relheight=0.06)
crlabel.place(x=220,y=480)
crac.place(x=870,y=480)



w.mainloop()
