def qtd_divisores(n:int)->int:
    """Dado um número inteiro n, calcula e retorna a quantidade de divisores que n tem."""
    divisores=[]
    for numero in range(1,n+1):
        if n%numero==0:
            list.append(divisores,numero)
    return len(divisores)