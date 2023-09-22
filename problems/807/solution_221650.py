def conta_frases(frase):
    a = str.partition(frase,'.')
    list.remove(a,'.')
    b = str.partition(frase[1],'!')
	list.remove(frase[1],'!')   
    return b