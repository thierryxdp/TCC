def inverte(frase):
    L = str.split(frase, " ")
    list.reverse(L)
	
    return str.join(" ", L)