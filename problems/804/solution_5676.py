def filtra_pares(t1,t2,t3,t4):
    tupla = [t1,t2,t3,t4]
    lista_filtrada = []
    for i in tupla:
        if i % 2 == 0:
            lista_filtrada.append(i)
    return lista_filtrada