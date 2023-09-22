def qtd_divisores(n):
    """Função que conta quantos divisores um numero tem,int-->int"""
    cont=0
    for x in range(1,n+1):
        if n % x ==0:
            cont += 1
    return cont