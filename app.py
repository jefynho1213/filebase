from src import Filebase

#Filebase.set_path("/home/diego/Code/filebase/data")

value = { "test" : "text test"  }

pack = Filebase("2017/03")

file_c = pack.update("test", value)

print(pack.read("test"))
