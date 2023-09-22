def qtd_divisores(n):
    '''int->int'''
    lista=[]
    i=1
    for i in list(range(1,n+1)):
        if n%i==0:
            list.append(lista,i)
            i=i+1
    return len(lista)