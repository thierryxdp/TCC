def faltante(y):
    '''funcao que retorna qual numero da sequencia esta faltando
    list->int'''
    i=0
    s=[]
    list.sort(y)
    while i<len(y)+1:
        s=s+[i+1,]
        i=i+1
    x= sum(s)
    w= sum(y)
    return x-w