def posLetra(frase,letra,p):
    ''' Dada uma frase temos uma função que procura posição da letra desejada na frase dando qual ocorrência desejada; str,str,str->str'''
    i=0
    lista= []
    while i<len(frase):
        if letra == frase[i]:
            lista += [i,]
        i = i + 1
    if p > len(lista):
        return -1
    else:
        return lista[p-1]