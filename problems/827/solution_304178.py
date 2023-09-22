def qtd_divisores(n):
    '''dado um número n, retorna quanros divisores esse número tem;
    int --> int'''
    lista=[]
    for num in range(1,n+1):
        if n%num==0:
            list.append(lista,num)
    return len(lista)