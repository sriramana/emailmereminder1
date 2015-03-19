import model
import datetime
import dateutil
from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil import parser
from google.appengine.api import mail

def sendmail():
	get_data = model.Reminder.query()
	#get_data.filter()
	for p in get_data.iter():
		date_par = p.date_inp
		futuredate = date_par + relativedelta( days=90)
		progress = (datetime.date.today()- date_par).days
		countdown = int(p.duration) - progress
		sender='g.sriramana@gmail.com'
		sender_name='Sri'
		receiver= p.email
		receiver_name= p.nickname
		mail.send_mail(sender="""%(sender_name)s <%(sender)s>"""%{'sender_name':sender_name,'sender':sender},
        		  	to="""%(receiver_name)s <%(to)s>"""%{'receiver_name':receiver_name,'to':receiver},
               		subject="""Countdown:%(counter)s"""%{'counter':countdown},
               		body="""You are %(counter)s days away. Hang tight till %(thisdate)s """%{'counter':countdown, 'thisdate':futuredate})