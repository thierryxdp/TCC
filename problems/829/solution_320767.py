def soma_h(N):
    """Função que calcula e retorna o valor de H com N termos, onde N é inteiro e é dado como entrada."""
    soma = 0
    for i in range(1,N+1):
        soma += (1/i)
    return round(soma, 2)