def faltante(lista):
	"""Retorna a peça que veio faltando. List -> int"""
    i = 0
    opa = range(1, len(lista)+1)
    while i < len(lista):
        if lista[i] != opa[i]:
            return opa[i]
        if lista[i] == opa[i] and i == len(lista)-1:
            return lista[i] + 1

        i = i + 1
	"""Era essa peça que você queria? - Jailson Mendes(1967-2018)"""