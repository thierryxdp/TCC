def faltante(lista):
    checagem = 0
    contador = 0
    while contador < len(lista):
        if lista[contador] != checagem+1:
            return lista[contador]
		contador = contador + 1