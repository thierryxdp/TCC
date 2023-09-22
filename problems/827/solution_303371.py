def qtd_divisores (n):
    """Função que, dado um número, retorne quantos divisores ele possui
    entrada: int
    saída: int"""
    
    lista = list(range(1,n+1))
    divisores = 0
    
    for numero in lista:
        if n%numero == 0:
            divisores = divisores + 1
            
    return divisores