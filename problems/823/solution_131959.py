def faltante(elementos):
    lista = (list(range(elementos[-1] + 1)))[1:]
    if elementos == lista:
        list.append(elementos, (elementos[-1] + 1))
        return elementos
    else:
        contador = 0
		while contador < len(elementos):
            if elementos[contador] == lista[contador]:
                contador = contador + 1
            elif elementos[contador] != lista[contador]:
                return elementos[contador] + 1