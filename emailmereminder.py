import os
import jinja2
import datetime
import dateutil
import wsgiref.handlers
import webapp2
import model
import email_cron

from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil import parser
#from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from google.appengine.api import users
#from google.appengine.ext import ndb

template_env = jinja2.Environment(
		loader=jinja2.FileSystemLoader('templates'),
		extensions=['jinja2.ext.autoescape'],
		autoescape=True)

# class Reminder(ndb.Model):
# 	nickname = ndb.StringProperty()
# 	email = ndb.StringProperty()
# 	date_inp = ndb.DateProperty()
# 	duration = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
	def get(self):
		template = template_env.get_template('home.html')
		self.response.out.write(template.render())
				
	def post(self):
		date_inp= parser.parse(self.request.get("date_inp"))
		futuredate = date_inp + relativedelta( days=90)
		progress = (datetime.datetime.today()- date_inp).days
		countdown = 90 - progress
		sender='sender@email'
		sender_name='Sri'
		receiver='receiver@email'
		receiver_name='Nmae'
		post_reminder = model.Reminder()
		post_reminder.nickname = self.request.get("nickname")
		post_reminder.email = self.request.get("email")
		post_reminder.date_inp = date_inp
		post_reminder.duration = self.request.get("duration")
		post_reminder.put()
		# mail.send_mail(sender="""%(sender_name)s <%(sender)s>"""%{'sender_name':sender_name,'sender':sender},
  #             to="""%(receiver_name)s <%(to)s>"""%{'receiver_name':receiver_name,'to':receiver},
  #             subject="""Countdown:%(counter)s"""%{'counter':countdown},
  #             body="""

		# 		You are %(counter)s days away. Hang tight till %(thisdate)s

		# """%{'counter':countdown, 'thisdate':futuredate})
		email_cron.sendmail()
		self.response.out.write("<h2> MAIL SENT SUCCESSFULLY</h2>")


application = webapp2.WSGIApplication([('/', MainPage)],
                                     debug=True)

def main():
  	run_wsgi_app(application)

if __name__ == "__main__":
  	main()
									
