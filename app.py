from src import Filebase


value = { "test" : "text test"  }

pack = Filebase("/var/www/html/dev/filebase/data")

pack.create("test", value)
pack.set_collection("2013/03")

file_c = pack.create("test", value)

print(pack.read("test"))
