def inverte(string):
    x=str.lower(string)
	x=str.replace(x,'.','')
    x=str.replace(x,',','')
    x=str.replace(x,'!','')
    x=str.replace(x,'?','')
    x=str.replace(x,'-',' ')
    return x