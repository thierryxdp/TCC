def soma_h(n):
    ''' Função que retorna a solução de uma conta de progressão aritmética.
    int=> int '''
    i = 1
    numero = 0.0
    for i in range(1, n+1):
        numero = numero + 1/i;
    return round(numero,2)