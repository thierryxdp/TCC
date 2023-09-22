def faltante(lista):
    contador = 0
    nova_lista = sorted(lista)

    while contador < len(lista):
        if contador + 1 == nova_lista[contador]:
            contador += 1

        else:
            return contador + 1

    return contador + 1