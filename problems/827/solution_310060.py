def qtd_divisores(n):
    """Função retorna quantos divisores um número tem"""
    for i in range(1, int(n/2+1)):
        if n % i == 0: 
            return i
    return n