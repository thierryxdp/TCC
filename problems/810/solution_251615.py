def inverte(c):
	x=str.lower(c)
	list.reverse(x)
    z=x.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ").replace(":"," ").replace("-"," ").replace(";"," ")
    return z