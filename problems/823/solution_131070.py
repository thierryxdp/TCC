def faltante(lista):
    contador = -1
    x = len(lista) + 1
    for n in range(x):
        contador +=1
        if n != lista[contador]:
            return lista[contador]