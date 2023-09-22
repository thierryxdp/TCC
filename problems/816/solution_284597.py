def maiores(lista_int,n):
    if lista_int[-1] < n:
     del lista_int[-1]
    if lista_int[-2] < n:
     del lista_int[-2]
    if len(lista_int) >= 3 and lista_int[-3] < n :
     del lista_int[-3]
    if len(lista_int) >= 4 and lista_int[-4] < n :
     del lista_int[-4]
    if len(lista_int) >= 5 and lista_int[-5] < n :
     del lista_int[-5]
    if len(lista_int) >= 6 and lista_int[-6] < n :
     del lista_int[-6]
    if len(lista_int) >= 7 and lista_int[-7] < n :
     del lista_int[-7]
    if len(lista_int) >= 8 and lista_int[-8] < n :
     del lista_int[-8]
    if len(lista_int) >= 9 and lista_int[-9] < n :
     del lista_int[-9]
    if len(lista_int) >= 10 and lista_int[-10] < n :
     del lista_int[-10]
    list.sort(lista_int)
    return lista_int