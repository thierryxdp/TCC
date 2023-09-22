def filtra_pares (a,b,c,d,):
    """função que recebe uma tupla com os elementos inteiros a, b,c e d e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam.
    int, int, int, int -> tupla"""
    tupla1= (a,)
    tupla2= (b,)
    tupla3= (c,)
    tupla4= (d,)
    novaTupla = ()
    if a%2==0:
        novaTupla = novaTupla + tupla1
    if b%2==0:
        novaTupla = novaTupla + tupla2
    if c%2==0:
        novaTupla = novaTupla + tupla3
    if d%2==0:
        novaTupla = novaTupla + tupla4
    return novaTupla 
         #Start your python function here