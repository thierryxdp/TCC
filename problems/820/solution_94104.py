def posLetra(texto, letra, numero):
    '''str,str,int->int'''
    proximo=0
    posicao=[]
    if texto.count(letra) < numero:
        return -1
    while proximo < len(texto):
        if texto[proximo] == letra:
            posicao.append(proximo)
        proximo=proximo+1
    return posicao[numero-1]