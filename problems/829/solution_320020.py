def soma_h (n):
    """Função que, dado um número 'n' de termos como entrada, calcula e retorna o valor de H da da função
    H = 1 + 1/2 + 1/3 + ... + 1/n
    Entrada: int
    Saída: float"""
    
    soma = 0
    for num in range(1,n+1):
        soma = soma + (1/num)
        
    somafinal = round(soma,2)
    return somafinal