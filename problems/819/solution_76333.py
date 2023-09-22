def filtraMultiplos (lista , n):
    lista2 = ''
    i = 0
    for i in lista:
        i % n ==0
        lista2 = lista2+ str (lista[i])
    i = i + 1
    return lista2