def soma_h(N):
    '''Função que dado um número "N" de entrada, retorna o valor "H" do
    somatório dos N termos.
    Essa função é baseada na equação que foi dada
    no enunciado da questão'''
    soma_total = 0
    for numero in range(1, N+1):
        soma_total += 1/numero
    return round(soma_total, 2)