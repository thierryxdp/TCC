def posLetra(frase,letra,numero):
    '''retorna a posição da string na ocorrencia desejada
    ent-int
    saida-int
    '''
    if frase.count(letra)<numero:
        return -1
    i=0
    n=0
    while n!=numero:
        if letra==frase[i]:
            posicao=i
            n+=1
        i+=1
    return posicao