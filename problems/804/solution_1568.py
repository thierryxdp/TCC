#Start your python function here
def filtra_pares(a,b,c,d):
    '''Dados os elementos a,b,c,d retorna uma nova tupla contendo apenas
    os elementos pares fornecidos; (int, int, int, int) -> (int,)'''
    tupla = ()
    if a%2 == 0:
        tupla = tupla + (a,)
    if b%2 == 0:
        tupla = tupla + (b,)
    if c%2 == 0:
        tupla = tupla + (c,)
    if d%2 == 0:
        tupla = tupla + (d,)
        return tupla