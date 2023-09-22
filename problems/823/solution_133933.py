def faltante(lista):
    list.sort(lista)
    contador = 0
    while contador < len(lista)-1:
        if lista[contador] + 1 != lista[contador + 1]:
            return lista[contador] + 1
        contador = contador + 1
    return lista[contador] + 1