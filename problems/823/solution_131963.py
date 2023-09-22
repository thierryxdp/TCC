'''Programa recebe a lista de peças do quebra-cabeças do menino e retorna o element
faltante da lista. Isto é, em uma sequência, qual o elemento que falta para que esta
esteja completa, ou então, qual o elemento que falta para compoletar a sequência.
list -> int'''
def faltante(elementos):
    lista = (list(range(elementos[-1] + 1)))[1:]
    if elementos == lista:
        list.append(elementos, (elementos[-1] + 1))
        return elementos[-1]
    else:
        contador = 0
		while contador < len(elementos):
            if elementos[contador] == lista[contador]:
                contador = contador + 1
            elif elementos[contador] != lista[contador]:
                return lista[contador]