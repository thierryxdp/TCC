def qtd_divisores(n):
    """Função que retorna a quantidade de divisores de um número inserido"""
    n_divisores=0
    for d in range(1,n+1):
        if n%d==0:
            n_divisores=n_divisores+1
    return n_divisores