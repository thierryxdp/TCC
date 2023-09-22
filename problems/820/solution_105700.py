def posLetra(x,y,z):
    """A funcao, dada como entrada uma frase, uma e o numero de ocorrencia dessa letra
    retorna a posiçao da letra na strig inicial na ocorrencia desejada.str,str,int-->int"""
    if str.count(x,y) < z:        
        return -1
    lista = list(range(len(x)))
    lista[:] = x
    indice = []    
    i = 0
    while i < len(lista) and len(indice) != z:
        pos1 = lista.index(y,i)
        indice = indice + [pos1]
        i = pos1 + 1    
    return indice[z-1]