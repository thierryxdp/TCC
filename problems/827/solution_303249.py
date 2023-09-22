def qtd_divisores(n):
    '''dado um número n, conta quantos divisores esse número tem;int->int'''
    lista=[]
    for c in range(1,n+1):
        if n%c==0:
            list.append(lista,c)
        
    return len(lista)