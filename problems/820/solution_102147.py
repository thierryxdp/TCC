def posLetra(frase,letra,ocorrencia):
    """função que recebe uma frase, uma letra e um 
    núemro que indica a ocorrência desejada da letra e
    retorna em que posição da letra aquela ocorrência
    da letra esta.
    str,str,int -> int"""
    lista = list (frase)
    cont = lista.count(letra)
    
    if cont >= ocorrencia:
    	substitui = str.replace(frase,letra,'&',ocorrencia - 1)
    	return str.find(substitui,letra,0,-1)
    else:
        return -1