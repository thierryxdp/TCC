def qtd_divisores(n):
    """Dado um número inteiro positivo n, retorna a quantidade de divisores
    positivos de n;
    int->int"""
    lista_divisores=[]
    for num in range(1,n+1):
        if n%num==0:
            lista_divisores.append(num)
    return len(lista_divisores)