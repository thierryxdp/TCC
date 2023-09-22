def posLetra(frase, letra, n):
    '''retorna a posicao da ocorrencia n de uma letra na frase
    str, str, int -> int'''
    pos=str.find(letra)
    while str.find(letra)>=0 and n>1:
        if letra!= frase:
            return -1
        pos=str.find(letra, pos+1)
        n=n-1
    return pos