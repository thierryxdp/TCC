def posLetra(frase,letra,numero):
    '''funcao que retorna em que posicao da string uma
    ocorrencia de letra esta. caso exista menos
    ocorrencias da letra do que a ocorrencia pedida 
    retorna -1'''
    f = list(frase)
    g = list.count(f,1)
    h = 0
    i = list.index(f,letra,h)
    p = 1
    if numero>g or g == 0:
        return -1
    while p<numero:
        h=i+1
        i=list.index(f,letra,h)
        p=p+1
    return i