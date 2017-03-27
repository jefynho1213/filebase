import os
import msgpack
import pandas as pd

class Filebase(object):
	path_default = "/tmp/filebase"

	def __init__(self, path):
		self.path_default = path

	def set_collection(self, collection):
		if not os.path.exists(self.path_default):
			os.makedirs(self.path_default)
		self.collection = self.path_default + "/" + collection

	def create(self, index, value):
		if self.created_path(self.collection) :
			_file = self.collection + "/" + index
			if os.path.isfile(_file + ".fbd") or os.path.isfile(_file + ".pd.fbd"):
				raise Exception("Error: index exist. Use update for modify file")
			else:
				if type(value) is pd.DataFrame:
					serialized = msgpack.packb(value.to_dict(orient='list'))
					with open(_file + ".pd.fbd", "wb") as file:
						file.write(serialized)
				else:
					serialized = msgpack.packb(value)
					with open(_file + ".fbd", "wb") as file:
						file.write(serialized)
		return True

	def read(self, index):
		_file = self.collection + "/" + index
		if os.path.isfile(_file + ".fbd"):
			with open(_file + ".fbd", "rb") as file:
				unFile = msgpack.unpackb(file.read())
				return unFile
		elif os.path.isfile(_file + ".pd.fbd"):
			with open(_file + ".pd.fbd", "rb") as file:
				unFile = msgpack.unpackb(file.read())
				return pd.DataFrame.from_dict(unFile)
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