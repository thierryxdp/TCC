def soma_h(n):
    '''Função retorna uma soma esquisita em que, dado um numero,
    ele soma todas as operações de: 1 divido pela lista de numeros
    que vem antes do termo n, incluindo o próprio n
    int -> float'''
    soma = 0
    for numero in range(1, n+1):
        soma += 1 / numero
        
    return round(soma, 2)