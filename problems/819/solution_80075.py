def filtraMultiplos (lista, n):
    '''funcao que retorne uma lista com multiplos de n'''
    for c in lista: 
    if c % n == 0: 
        lista.append(c)
    return (lista)