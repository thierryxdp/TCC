def soma_h(N):
    'Dado um número inteiro N, calcula o valor da série H para os N primeiro termos. Entrada: int. Saída: float.'
    soma=0
    for variavel in range(N+1):
        soma=soma+(1/N)
    return soma