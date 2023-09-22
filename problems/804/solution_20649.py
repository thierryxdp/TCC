def filtra_pares(x):

    """Retorna uma tupla de números pares dada uma tupla de 4 inteiros como
    input. O output será uma tupla com os elementos pares na mesma ordem que
    a do input, se não houver elemento par é retornado uma tupla vazia.
    assintura: tuple--->tuple
    testes:
    filtra_pares((1,1,1,1))==()
    filtra_pares((1,2,1,2))==(2,2)
    filtra_pares((1,2,1,3))==(2,)
    filtra_pares((18,1,1,3))==(18,)
    filtra_pares((18,1,18,3))==(18,18)
    filtra_pares((1,4,1,1))==(4,)
    
    """
    tupla = ()
    if x[0] % 2 == 0:
        tupla = tupla + (x[0],)
    if x[1] % 2 == 0:
        tupla = tupla + (x[1],)
    if x[2] % 2 == 0:
        tupla = tupla + (x[2],)
    if x[3] % 2 == 0:
        tupla = tupla + (x[3],)
    return tupla