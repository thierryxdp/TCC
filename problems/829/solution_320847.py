def soma_h(n):
    """Funcao que calcula e retorna o valor de H = 1 + 1/2 + 1/3 ... + 1/n com n 
    	termos onde n é inteiro e dado como entrada."""
    soma = 0
    for i in range(1, n + 1):
        inverso = (1/i)
        soma += inverso
    return round(soma, 2)