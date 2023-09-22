def inverte(c):
    b=c.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ").replace(":"," ").replace("-"," ").replace(";"," ")
	x=str.lower(b)
	list.reverse(x)
    return x