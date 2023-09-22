def faltante(lista):
    checagem = 1
    contador = 0
    while contador < len(lista):
        if lista[contador] != checagem:
            return checagem
        else:
            contador = contador + 1
            checagem = checagem + 1