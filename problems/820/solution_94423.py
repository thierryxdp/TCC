def posLetra(frase,letra,numero):
    '''retorna a ocorrência de número 'numero' da letra pedidade dentro da frase'''
    if frase.count(letra)<numero:
        return -1
    i=0
    n=0
    while n!=numero:
        if letra==frase[i]:
            posição=i
            n+=1
        i+=1
    return posição