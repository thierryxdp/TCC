def divisao(n):
    
    soma = 0
    
    for i in range(1,n+1):
        soma = soma + (1/i)
    
    return soma

def soma_h(n: int) -> float:
    """Função que, dada a entrada como sendo um número inteiro, retorna o somatório de 
    1 + 1/2 + ... + 1/n"""
    
    numero = [n]
    somatorio = list(map(soma, numero))