def qtd_divisores(n):
    """Função retorna quantos divisores um número tem"""
    for i in range(1,n):
        if n % i == 0:
            return (i)