def soma_h(num):
    """retorna a soma um numero com N termos
    int -> flota"""
    soma = 0
    for numero in range(1,num+1):
        soma += 1/numero
    return round(soma,2)