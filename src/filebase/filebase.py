import os
import msgpack

class Filebase(object):
	path_default = "/tmp/filebase"

	def __init__(self, path):
		self.path_default = path


	def set_collection(self, collection):
		if not os.path.exists(self.path_default):
			os.makedirs(self.path_default)
		self.collection = self.path_default + "/" + collection


	# inseri arquivo no direfotio informado
	# [parametros]
	def create(self, index, value):
		if self.created_path(self.collection) :
			_file = self.collection + "/" + index + ".bin"
			if os.path.isfile(_file):
				print "Error : index exist. Use update for modify file"
				return False
			else:
				serialized = msgpack.packb(value)
				file = open(_file, "wb")
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

	def update(self, index, value):
		if self.created_path(self.collection) :
			_file = self.collection + "/" + index + ".bin"
			if not os.path.isfile(_file):
				print "Error : index not exist. Use create for create new file"
				return False
			else:
				serialized = msgpack.packb(value)
				file = open(_file, "wb")
				file.write(serialized)
				file.close()
				return True

	def created_path(self, path):
		if os.path.exists(path):
			return True
		else:
			os.makedirs(path)
			return True