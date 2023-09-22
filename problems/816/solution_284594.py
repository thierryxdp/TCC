def maiores(lista_int,n):
    if lista_int[-1] < n:
     del lista_int[-1]
    if lista_int[-2] < n:
     del lista_int[-2]
    if lista_int[-3] < n:
     del lista_int[-3]
    if lista_int[-4] < n:
     del lista_int[-4]
    return lista_int