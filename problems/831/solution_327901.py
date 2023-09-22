def lingua_p(palavra):
    '''Funcao que recebe uma palavra e a retorna traduzida
    para a lingua do P
    str -> str'''
    x = ''
    for elemento in palavra:
        if elemento in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            x += elemento + 'p' + elemento
        else:
            x += elemento
    return x