def qtd_divisores(n):
    '''retorna a quantidade de divisores que o número n tem.
    int -> int'''
    
    divisores=[]
    
    for numero in range(1, n+1):
        if n%numero==0:
            list.append(divisores, numero)
    return len(divisores)