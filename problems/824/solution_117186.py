def uppCons(texto):
	i=0
    str.upper(texto)
    while i<len(texto):
        str.replace(texto,'A','a')
        str.replace(texto,'E','e')
        str.replace(texto,'I','i')
        str.replace(texto,'O','o')
        str.replace(texto,'U','u')
        i=i+1
        return texto