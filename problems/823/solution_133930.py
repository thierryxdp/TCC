def faltante(lista):
    list.sort(lista)
    contador = 0
    while contador < len(lista):
        if lista[contador] != lista[contador + 1] - 1:
            return lista[contador] + 1
        contador = contador + 1