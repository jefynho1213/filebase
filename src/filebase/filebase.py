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
				raise Exception("Error: index exist. Use update() for modify file")
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
			_file = self.collection + "/" + index
			if os.path.isfile(_file + ".fbd") or os.path.isfile(_file + ".pd.fbd"):
				if type(value) is pd.DataFrame:
					serialized = msgpack.packb(value.to_dict(orient='list'))
					with open(_file + ".pd.fbd", "wb") as file:
						file.write(serialized)
				else:
					serialized = msgpack.packb(value)
					with open(_file + "fbd", "wb") as file:
						file.write(serialized)
			else:
				raise Exception("Error: index not exist. Use create() for create file")
		return True

	def insert(self, index, value):
		if self.created_path(self.collection):
			_file = self.collection + "/" + index
			if type(value) is pd.DataFrame:
				if os.path.isfile(_file + ".pd.fbd"):
					df_old = self.read(index)
					df_new =  pd.concat([df_old, value])
					self.update(index, df_new)
				else:
					raise Exception("Error: file is not format DataFrame")
			else :
				if os.path.isfile(_file + ".fbd"):
					file_old = self.read(index)
					file_new = file_old + value
					self.update(index, file_new)
				else:
					raise Exception("Error: file is format DataFrame")

	def schema(self, index):
		_file = self.collection + "/" + index
		if os.path.isfile(_file + ".pd.fbd"):
			df = self.read(index)
			_schmea = {
				"columns" : df.columns,
				"shape" : df.shape,
				"types" : df.ftypes,
				"memory" : df.memory_usage(),
			}
			return _schmea
		else:
			raise Exception("Error: file is not format DataFrame")


	def created_path(self, path):
		if os.path.exists(path):
			return True
		else:
			os.makedirs(path)
			return True