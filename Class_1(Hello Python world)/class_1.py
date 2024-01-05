name : list[str] = ['a','b','c','d','e','f',200]
print(name)
print(type(name))
print(id(name))
print(dir(name))
print(i for i in dir(name) if"__" not in i)

name : tuple[str,int,float] = ['ahsan hayat',5709,"A"]
print(name) # print
print(type(name)) # type
print(id(name))   # physical addres
print(dir(name))
print(i for i in dir(name) if"__" not in i) # methods and attributes


name : any = "python"
print(name) # print
print(type(name)) # type
print(id(name))   # physical addres
print(dir(name))
print(i for i in dir(name) if"__" not in i) # methods and attributes