def primo(n):
    '''função que dado um número inteiro positivo como entrada,
    verifica se o mesmo é primo ou não'''
    contador=0
    for i in range (1, num+1):
        if num % i == 0:
            contador = contador + 1
        if contador == 2:
            'É sim número primo!'
        else:
            'Não é número primo!'
        contador = 0