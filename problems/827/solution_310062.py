def qtd_divisores(num):
    """Função retorna quantos divisores um número tem"""
    n = np.arange(1,num)
    d = num % n
    zeros = d == 0
    return (n[zeros])