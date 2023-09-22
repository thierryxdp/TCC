def qtd_divisores(n):
    '''função que,dado um número n, retorna quantos divisores esse número tem;
    int -> int'''
    lista=[]
    for i in range(1,n+1):
        if n%i == 0:
            list.append(lista,i)
    return len(lista)