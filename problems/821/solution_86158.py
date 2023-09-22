def fatorial (n):
    ''' funcao ira receber um numero e retornar seu fatorial
    entrada: int  saida: int'''
    i = 1
    resultado = 1
    
    while i <= n:
        resultado = resultado * i 
        i = i + 1
    return resultado