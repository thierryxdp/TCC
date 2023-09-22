def faltante(lista):
    tamLista = len(lista) + 1
    num = 1
    while tamLista >= 1:
        num = num - tamLista
        tamLista = tamLista - 1
    return num