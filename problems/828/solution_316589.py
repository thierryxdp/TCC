def primo (N):
    ''' Uma funcao que dado um numero inteiro, diz se este numero é primo
    ou não. Retorna valor booleano.'''
    contador = 0
    for i in range(N):
        if N%(i+1)==0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False