import os
import cPickle as pickle


class Fb_query(object):

	path_default = "/var/www/html/dev/fbM2M/fb/"

	def __init__(self, collection):
		if not os.path.exists(self.path_default):
			os.makedirs(self.path_default)
		self.collection = self.path_default + collection

	# inseri arquivo no direfotio informado
	# [parametros]


	def created(self, index, value):
		

		if self.created_path(self.collection) :

			file = open(self.collection + "/" + index + ".bin", "w")
			pickle.dump(value, file)
			file.close()
			return True

	def read(self, index):

		_file = self.collection + "/" + index + ".bin"
		if os.path.isfile(_file):
			file = open(_file)
			unFile = pickle.load(file)
			file.close()
			return unFile
		else :
			return False
		


	def created_path(self, path):

		if os.path.exists(path):
			return True
		else :
			os.makedirs(path)
			return True
