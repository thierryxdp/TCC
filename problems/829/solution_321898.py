def soma_h(n):
    """Função que calcula e retorna o valor de H com N termos onde N é inteiro e dado como entrada,
    int --> float"""
    soma = 0
    for i in range(1, n+1):
        soma += 1/i
    
    return round(soma, 2)