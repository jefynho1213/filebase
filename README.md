# filebase

Filebase was thought to be a simple library to enable the storage of data without the necessity of database, its interaction with Pandas leaves it good for analytics. The storage is done through files with any data-type, but for the Pandas to it is necessary to write objects that extends the Pandas DataFrame class. The data is serialized using the msgPack library, so the read and write can be performed in a shorter time and achieved savings of 35% in storage size.

## Examples

#### dataFrame pandas

``` python
from src import Filebase
import os
import pandas as pd

#set file base path
pack = Filebase(os.getcwd() + "/data")

#set files collection path
#use "/" for create sub paths
pack.set_collection("2013/03")

#create data frame pandas
dataframe = pd.DataFrame({
    'a': pd.Series(range(10)),
    'b': pd.Series(range(10)),
    'c': pd.Series(range(10))
})

#create new file
#params: index, file value
pack.create("test7", dataframe)

#read file
file_c = pack.read("test7")

print(file_c)


```
[out]:
```shell
   a  b  c
0  0  0  0
1  1  1  1
2  2  2  2
3  3  3  3
4  4  4  4
5  5  5  5
6  6  6  6
7  7  7  7
8  8  8  8
9  9  9  9
```


#### Create

``` python
from src import Filebase
import os

value = { "test" : "text test"  }

#set file base path
pack = Filebase(os.getcwd() + "/data")

#set files collection path
#use "/" for create sub paths
pack.set_collection("2017/03")

# params: index, file value
pack.create("test", value)

print(pack.read("test"))

```
[out]:
```shell
{'test': 'text test'}
```

#### Update

``` python
from src import Filebase
import os

value = { "test" : "text test update"  }

#set file base path
pack = Filebase(os.getcwd() + "/data")

#set files collection path
#use "/" for create sub paths
pack.set_collection("2017/03")

#params: index, file value
pack.update("test", value)

print(pack.read("test"))

```
[out]:
```shell
{'test': 'text test update'}
```
