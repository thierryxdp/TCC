def soma_h(n):
    """Função que calcula um numero inteiro e retona o valor de H com N termos em que um numero inteiro é dado com entrada; inf -> float""" 
    soma = 0 
    i = 1 
    while i <= n:
        soma = soma + 1/i
        i = i + 1 
    return round(soma,2)