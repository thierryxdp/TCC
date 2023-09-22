def lingua_p(palavra):
    vogais = [ 'a', 'e', 'i', 'o', 'u']
    res=''
    for i in palavra:
    	if i in vogais:
            res=res+i+'p'+i
        else:
            res=res+i
    return res