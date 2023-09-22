def soma_h(N):
    '''Funcao que retorna o valor da soma H
    dado o numero de termos N.
    Dados de entrada: int
    Valor de saida: float
    '''
    soma = 0 #Em que soma é o H
    numerador = 1
    for numero in range(1,N+1):
        soma += numerador / numero
    return round(soma, 2)