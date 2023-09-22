def soma_h(n):
    """A funcao soma_h recebe um numero inteiro n e devolve a soma de uma lista de numeros 
    no formato de fracao, cujo denominador inicia-se em 1 e termina em n."""
    Soma = 0
    for i in range(1,n + 1):
        Soma = Soma + 1/i
    return round(Soma,2)