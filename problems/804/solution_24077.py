def filtra_pares(tup):
    '''Função que recebe uma tupla com quatro números inteiros
    e retorna uma nova tupla contendo os números pares da tupla
    original.
    tup->tup'''
    elem_pares=()
    if tup[0]%2==0:
        elem_pares=elem_pares+(tup[0],)
    if tup[1]%2==0:
        elem_pares=elem_pares+(tup[1],)
    if tup[2]%2==0:
        elem_pares=elem_pares+(tup[2],)
    if tup[3]%2==0:
        elem_pares=elem_pares+(tup[3],)