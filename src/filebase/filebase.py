import os
import msgpack
import pandas as pd

class Filebase(object):
	path_default = "/tmp/filebase"

	def __init__(self, collection):
		if not os.path.exists(self.path_default):
			os.makedirs(self.path_default)
		self.collection = self.path_default + "/" + collection

	def set_path(self, path):
		self.path_default = path

	def create(self, index, value):
		if self.created_path(self.collection) :
			_file = self.collection + "/" + index + ".bin"
			if os.path.isfile(_file):
				raise Exception("Error: index exist. Use update for modify file")
			else:
				serialized = msgpack.packb(value)
				
				with open(_file, "wb") as file:
					file.write(serialized)
		
		return True

	def read(self, index):
		_file = self.collection + "/" + index + ".bin"
		if os.path.isfile(_file):
			with open(_file) as file:
				unFile = msgpack.unpackb(file.read())
				return unFile
		return False

	def update(self, index, value):
		if self.created_path(self.collection) :
			_file = self.collection + "/" + index + ".bin"
			if not os.path.isfile(_file):
				raise Exception("Error: index not exist. Use create for create file")
			else:
				serialized = msgpack.packb(value)
				with open(_file, "wb") as file:
					file.write(serialized)
		return True

	def created_path(self, path):
		if os.path.exists(path):
			return True
		else:
			os.makedirs(path)
			return True