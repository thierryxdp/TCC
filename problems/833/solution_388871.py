def conta_numero(numero,matriz):
    '''Conta quantas vezes o numero especificado aparece na matriz
    int, list - int'''
    soma = 0
    for i in matriz:
        
        for n in i:
            if n == numero:
                soma = soma + 1

        
    return soma