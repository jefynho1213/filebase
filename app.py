from src import Filebase
import pandas as pd

pack = Filebase("/home/diego/Code/filebase/data")

pack.set_collection("2013/03")

dataframe = pd.DataFrame({
    'a': pd.Series(range(10)),
    'b': pd.Series(range(10)),
    'c': pd.Series(range(10))
})

pack.create("test7", dataframe)

file_c = pack.read("test7")

print(file_c)
