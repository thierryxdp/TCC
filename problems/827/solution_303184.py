def qtd_divisores(n):
    '''funcao que conta e retorna quandos divisores um numero tem
    int->int'''
    i=1
    divisores=[]
    for elemento in range(n):
        if n%i == 0:
            list.append(divisores,i)
        i=i+1
    return len(divisores)