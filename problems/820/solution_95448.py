def posLetra(frase,letra,numero):
    '''retorna a posição da string na ocorrencia
    string,string,int->int'''
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