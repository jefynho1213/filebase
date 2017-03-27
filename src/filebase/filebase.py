import os
import msgpack

class Filebase(object):
	path_default = "/tmp/filebase"

	def __init__(self, collection):
		if not os.path.exists(self.path_default):
			os.makedirs(self.path_default)
		self.collection = self.path_default + "/" + collection

	def set_path(self, path):
		self.path_default = path

	# inseri arquivo no direfotio informado
	# [parametros]
	def create(self, index, value):
		if self.created_path(self.collection) :
			serialized = msgpack.packb(value)
			file = open(self.collection + "/" + index + ".bin", "wb")
			file.write(serialized)
			file.close()
			return True

	def read(self, index):
		_file = self.collection + "/" + index + ".bin"
		if os.path.isfile(_file):
			file = open(_file).read()
			unFile = msgpack.unpackb(file)
			return unFile
		else:
			return False

	def created_path(self, path):
		if os.path.exists(path):
			return True
		else:
			os.makedirs(path)
			return True