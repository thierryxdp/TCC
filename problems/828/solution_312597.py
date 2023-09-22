def primo(numero):
    'função que dado um numero verifica se ele é ou não primo'
    divisores = 0
    for i in range(1, numero+1):
        if numero%i == 0:
            divisores = divisores + 1
    if divisores == 2:
        return True
    else:
        return False