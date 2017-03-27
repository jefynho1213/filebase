# filebase

## Examples
##### create
____
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
> [filebase]$ python2.7 app.py
>
> {'test': 'text test'}


##### update
____
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
> [filebase]$ python2.7 app.py
>
> {'test': 'text test update'}
