from google.appengine.ext import ndb

class Reminder(ndb.Model):
	nickname = ndb.StringProperty()
	email = ndb.StringProperty()
	date_inp = ndb.DateProperty()
	duration = ndb.StringProperty()
	complete = ndb.StringProperty(default='N')