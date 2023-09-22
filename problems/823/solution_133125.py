def faltante(l):
    ''' Função que informa que peça está faltando de um quebra-cabeças a partir de uma lista l
    que contem a numeração das peças. list->int'''
    i=0
    s=0
    n=len(l)
    x=list(range(1,n+1))
    while(i<n+1):
        s=s+(l[i]-x[i])
        i=i+1
    return s