def qtd_divisores(n):
    """Função que tem como retorno o número de divisores de um número n, int -> int"""
    contador_divisores = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            contador_divisores += 1
    
    return contador_divisores