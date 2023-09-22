def posLetra(frase,letra,ocorrencia):
    '''diz a posição de uma letra dada a ocorrencia. str,str,int->int'''
    a=list(frase)
    b=frase.count(letra)
    if b<ocorrencia:
        return -1
    i=0
    c=[]
    d=[]
    while i<len(frase):
        if letra in frase:
            c.append(frase.index(letra))
            a.pop(c[i])
            a.append(c[i],(letra + str(i+1))
        i=i+1
    return a.index(letra + str(ocorrencia))