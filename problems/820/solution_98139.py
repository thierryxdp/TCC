def posLetra(frase,letra,numero):
    '''identifica onde está a ocorrencia desejada da letra na frase
    str,str,int -> int'''
    frase = list(frase)
    proximo = 0
    qtletra = 0
    while qtletra < numero and proximo < len(frase):
        if frase[proximo] == letra:
            qtletra += 1
            frase[proximo] = '.'
    	proximo += 1
    if letra not in frase:
        return -1
    if qtletra == 0:
        return -1
    return list.index(frase,letra)