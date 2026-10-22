import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
t=tkinter.Tk()
t.geometry("800x800")
def sendgmail():
    from_address = "rashikag43@gmail.com"
    to_address = e2.get()
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Filename"+e1.get()
    msg['From'] = from_address
    msg['To'] = to_address
    
    # Create the message (HTML)
    f=open(e1.get(),"r")
    s=f.read()
    f.close()
    Text = 'Content are <Br>'+s
    
    # Record the MIME type - text/html.
    part1 = MIMEText(Text, 'html')
    
    # Attach parts into message container
    msg.attach(part1)
    
    # Credentials
    username = 'rashikag43@gmail.com'  
    password = 'sjzu vora gkaj krcg'
    
    # Sending the email
    ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login(username,password)  
    server.sendmail(from_address, to_address, msg.as_string())  
    server.quit()
    messagebox.showinfo('Hi','Mail Send')

a=Label(t,text="FileName")
a.place(x=50,y=20)
e1=Entry(t, width =30)
e1.place(x=400,y=50)
b=Label(t,text="Email")
b.place(x=50,y=80)
e2=Entry(t, width =30)
e2.place(x=400,y=80)
bt=Button(t,text="Send", command=sendgmail)
bt.place(x=100,y=150)
t.mainloop()