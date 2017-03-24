from src.filebase.filebase import *

value = { "test" : "text test"  }
pack = Fb_query("2017/03")

pack.created("test" , value)

print pack.read("test")
