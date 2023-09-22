def qtd_divisores(numero):
    """Função que retorna a quantidade de divisores que um número tem dado ele como parâmetro. Entrada -> int; Saída -> int"""
    
    divisores = []
    
    for divisor in range(1, numero+1):
        if numero % divisor ==0:
            divisores = divisores + [divisor,]
    
    return len(divisores)