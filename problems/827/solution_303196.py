def qtd_divisores(n):
    '''funcao que conta e retorna quandos divisores um numero tem
    int->int'''
    i=1
    divisores=[]
    for n in range(n,n+1):
        if n%i == 0:
            list.append(divisores,i)
    return len(divisores)