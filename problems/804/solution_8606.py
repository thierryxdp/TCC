def filtra_pares (tupla):
    """função que recebe uma tupla com os elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam.
    int, int, int, int -> tupla"""
    tupla3 = ()

    if (tupla[0]%2) == 0:
        x = tupla[0]
        tupla2 = (x,)
        tupla3 = tupla3 + tupla2
    if (tupla[1]%2) == 0:
        x = tupla[1]
        tupla2 = (x,)
        tupla3 = tupla3 + tupla2
    if (tupla[2]%2) == 0:
        x = tupla[2]
        tupla2 = (x,)
        tupla3 = tupla3 + tupla2
    if (tupla[3]%2) == 0:
        x = tupla[3]
        tupla2 = (x,)
        tupla3 = tupla3 + tupla2
    return (tupla3)

         #Start your python function here