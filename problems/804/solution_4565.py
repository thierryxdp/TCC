def filtra_pares(x, y, z, w):
    '''Função que, dados quatro elementos inteiros como parâmetro, retorna um tupla contendo apenas os elementos pares da tupla original na mesma ordem que se encontravam; int, int, int, int -> tuple.'''
    tupla = (x, y, z, w)
    if (tupla[0] % 2 == 0):
        return tupla[0]
    if (tupla[1] % 2 == 0):
        return tupla[1]
    if (tupla[2] % 2 == 0):
        return tupla[2]
    if (tupla[3] % 2 == 0):
        return tupla[3]
    return tupla[0] + tupla[1] + tupla[2] + tupla[3]