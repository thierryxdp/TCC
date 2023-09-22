def soma_h(n):
    """funcao que calcula e retorna o valor de H com N termos onde o n e um numero inteiro e
    dado como entrada;
    int -> float"""
    acumulador = 0
    for i in range (1, n+1):
        H = i/1
        acumulador += H
        
    return round(acumulador, 2)