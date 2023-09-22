def repetidos(listaNum):
    """Calcula e retorna o numero de vezes que um 
    elemento da listaNum eh igual ao elemento anterior;
    list-->int"""
    i=0
    repeticao=0
    while i<len(listaNum):
			if listaNum[i] == listaNum[i-1]:
            repeticao = repeticao+1
            i=i+1
    return repeticao