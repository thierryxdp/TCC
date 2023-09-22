def soma_h(n):
    """ Função que calcula e retorna o resultado de uma soma H com n termos.
    int --> float"""
    i = 0
    resultado = 0
    for num in range(n):
        i = i+1
        resultado = resultado + (1/i)
        
    return round(resultado, 2)