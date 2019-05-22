import json
from smtplib import SMTP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'email'
email_password = 'passowrd' #can be application specific
def send_email(member, task, email_send):
	

	msg = MIMEMultipart()
	msg['From'] = email_user
	msg['To'] = email_send
	msg['Subject'] = "Action-Tracker"
	text_ = "<th><tr><td>Task</td><td>Status</td></tr></th>"
	for i in task["tasks"]:
		text_+="<tr>"+"<td>"+i["task"]+"</td>"+"<td>"+i["status"]+"</td>"+"</tr>"
	body ="<html><body><p>This email is about your current work status. For futher information please check your Action task tracker, your new task is</p><table border='5'>"+ text_+"</table></body></html>"
		
	
	

	msg.attach(MIMEText(body,'html'))
	text = msg.as_string()
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(email_user,email_password)
	server.sendmail(email_user,email_send,text)
	server.quit()