def faltante(x):
    '''Função que dada um lista retorna o número que está faltando
       list->int'''
    i=0
    b=[]
    while i<=len(x):
        i+=1
        if x.count(i)==0:
            b.append(i)
    return b