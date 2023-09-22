def filtra_pares(elem1, elem2, elem3, elem4):
    '''Recebe tupla com quatro inteiros e retorna uma
    tupla com apenas os elementos pares, na ordem 
    original
    int, int, int, int -> tuple'''
    tupla = ()
    if elem1 % 2 == 0:
        tupla = tupla + (elem1,)
    elif elem2 % 2 == 0:
        tupla = tupla + (elem2,)
    elif elem3 % 2 == 0:
        tupla = tupla + (elem3,)
    elif elem4 % 2 == 0:
        tupla = tupla + (elem4,)
    
    return tupla