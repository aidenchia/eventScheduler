import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	CSRF_ENABLED = True	
	SECRET_KEY = os.urandom(12)
	

class ProductionConfig(Config):
	DEBUG = True


