def posLetra (trecho,letra,numero):
    '''retorna em que posição da string aquela ocorrencia da letra esta
    str,str,int->int'''
    i=0
    j=0
    k=0
    while i<len(trecho):
        if letra==trecho[i]:
            j=j+1
            if numero==j:
                k=str.find(trecho,letra,numero)
        i=i+1
    return k