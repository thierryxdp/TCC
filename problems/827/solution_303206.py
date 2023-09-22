def qtd_divisores(n):
    """Pede um número inteiro e retorna a quantidade
    de seus divisores naturais
    int->int"""
    divisores=[]
    for x in range(1,n+1):
        if n%x == 0:
            divisores.append(x)
    return len(divisores)