def faltante(l):
    ''' Função que analisa uma lista l que contem a identificação das peças
    de um quebra-cabeças e informa que peça falta.
    list->int'''
    i=0
    n=len(l)
    s=[]
    t=l+list(range(1,n+1))
    list.sort(t)
    while(i<n):
        if(t[i]!=t[(i-1)]):
            list.append(s,t[i])
        i=i+1
    x=len(s)
    return s[x]