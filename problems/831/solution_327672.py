def lingua_p(palavra):
    vogais = [ 'a', 'e','ê','é','â','á','ú','i','í', 'o', 'u']
    res=''
    for i in palavra:
    	if i in vogais:
            res=res+i+'p'+i
        else:
            res=res+i
    return res