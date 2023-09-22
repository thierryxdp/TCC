def filtra_pares(tup):
    #Funcao que recebe uma tupla e retorna os numeros pares dentro dela. (tupla -> tulpa)
    lista = []
    if tup[0]%2 == 0:
        lista.append(tup[0])
    if tup[1]%2 == 0:
        lista.append(tup[1])
    if tup[2]%2 == 0:
        lista.append(tup[2])
    if tup[3]%2 == 0:
        lista.append(tup[3])
    return tuple(lista)