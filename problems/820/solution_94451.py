def posLetra(frase,letra,ocorrencia):
    '''diz a posição de uma letra dada a ocorrencia. str,str,int->int'''
    a=list(frase)
    b=frase.count(letra)
    if b<ocorrencia:
        return -1
    i=0
    c=[]
    while i<len(frase):
        c.append(a.index(letra,i))
        i=i+1
    return a[c[ocorrencia-1]]