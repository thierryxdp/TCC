def soma_h(N):
    '''Função que dado um número "N" de entrada, retorna o valor "H" do
    somatório dos N termos.
    Essa função é baseada na equação que foi dada
    no enunciado da questão'''
    soma_total = 0
    for numero in range(0, N+1):
        soma_total += (-1.0)**numero/(2*numero + 1)
    return round(soma_total, 2)