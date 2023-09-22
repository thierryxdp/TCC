def filtraMultiplos (lista, n):
    '''funcao que retorna multiplos de um numero'''
    for x in range(1, n):
        if (n % x == 0): #se o resto da divisão de n/x for 0 (múltiplo)
        return x