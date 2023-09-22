def qtd_divisores(n):
    '''função que verifica e retorna quantos divisores um número n possui; int -> int'''
    
    divisores = []
    for i in range(1,n+1):
        if n%i == 0:
            divisores.append(i)
    return len(divisores)