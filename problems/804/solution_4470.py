def filtra_pares(x, y, z, w):
    '''Função que, dados quatro elementos inteiros como parâmetro, retorna um tupla contendo apenas os elementos pares da tupla original na mesma ordem que se encontravam; int, int, int, int -> tuple.'''
    tupla = (x, y, z, w)
    tupla_par = ()
    if (tupla[0] % 2 == 0):
        tupla_par[:] + tupla[0]
    if (tupla[1] % 2 == 0):
        tupla_par[:] + tupla[1]
    if (tupla[2] % 2 == 0):
        tupla_par[:] + tupla[2]
    if (tupla[3] % 2 == 0):
        tupla_par[:] + tupla[3]
    return tupla_par