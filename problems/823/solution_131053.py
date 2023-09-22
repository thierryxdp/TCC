def faltante(lista):
    contador = 0
    x = len(lista)
    for n in range x+1:
        contador +=1
        if n != lista[contador]:
            return n