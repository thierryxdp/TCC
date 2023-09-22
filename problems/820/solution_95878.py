def posLetra(frase,letra,ocorrencia):
    '''Retorna a posicao da enesima ocorrencia da letra
    na frase
    str,str,int->int'''
    total = frase.count(letra)
    if total < ocorrencia:
        return -1
    else:
        pos = -1
        while ocorrencia > 0:
            pos = frase.index(letra,pos+1)
            ocorrencia = ocorrencia - 1
        return pos