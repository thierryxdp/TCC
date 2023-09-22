def faltante(n):
    '''funçao que retorna o numero faltante de um intervalo;list->int'''
    i=0
    x=[]
    list.sort(n)
    while i<len(n)+1:
        x=x+[i+1,]
        i=i+1
    a=sum(x)
    b=sum(n)
    return a-b