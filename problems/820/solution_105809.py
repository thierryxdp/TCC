def posLetra (trecho,letra,numero):
    '''retorna em que posição da string aquela ocorrencia da letra esta
    str,str,int->int'''
    i=0
    j=0
    k=-1
    while i<len(trecho):
        if letra==trecho[i]:
            j=j+1
            if numero==j:
                k=str.find(trecho,letra,(numero)-1)
        i=i+1
    return k