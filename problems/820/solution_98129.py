def posLetra(frase,letra,numero):
    '''identifica onde está a ocorrencia desejada da letra na frase
    str,str,int -> int'''
    proximo = 0
    qtletra = 0
    while qtletra < numero - 1 or proximo > len(frase):
        if frase[proximo] == letra:
            qtletra += 1
            str.replace(frase,frase[proximo],'.')
    	proximo += 1
    if qtletra == 0:
        return -1
    frase = list(frase)
    return list.index(frase,letra)