def inverte(string):
    x=str.lower(string)
	x=str.replace(x,'.','')
    x=str.replace(x,',','')
    x=str.replace(x,'!','')
    x=str.replace(x,'?','')
    x=str.replace(x,'-',' ')
    x=list.reverte(x)
    return x