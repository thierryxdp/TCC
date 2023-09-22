def primo(x):
    'funcao que dado um numero verifica se ele é primo ou nao e retorna um booleano.int->bool'''
    numerosprimos=0
    for i in range(1, x + 1):
        if x % i == 0:
            numerosprimos += 1
    if numerosprimos ==2:
        return True
    else:
        return False