def faltante(lista):
    contador = 0
    for n in range len(lista)+1:
        contador +=1
        if n != lista[contador]:
            return n