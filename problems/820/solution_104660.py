def posLetra(String,Letra,n):
    '''retorna posição n da String em que ocorre tal Letra
    str,str,int->int'''
    i=0
    palavra=()
    while i<len(String):
        if palavra in Letra:
        	return palavra
        i=i+1
    return i