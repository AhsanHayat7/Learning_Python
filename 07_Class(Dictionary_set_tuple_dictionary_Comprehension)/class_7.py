from typing import Dict, Union,Optional
import pprint

key : Union[int,float,str] # Creat custom data type
value : Union[str,str,list,dict,tuple,set]

data : dict[str,str]  = {
                        "King":"Lion",
                        "Sea King":"Whale",
                        "Sky King":"Eagle" 
                        }


print(data["King"]) # Key 
print(data["Sky King"])
data["Human"] = "King Of World"
print(data)
data["King"] = "Tiger"
data
del data["King"]
data


pprint.pprint(data)