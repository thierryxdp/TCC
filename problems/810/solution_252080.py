def inverte(string):
    x=str.lower(string)
	x=str.replace(x,'.','')
    x=str.replace(x,',','')
    x=str.replace(x,'!','')
    x=str.replace(x,'?','')
    x=str.replace(x,'-',' ')
    x=str.split(x)
    return list.reverse(x)