def busca (setor, lista):
    'dada uma lista com os dados dos funcionários de uma empresa, retorna os dados dos funcionários do setor infromado. str -> str'
    lista2 = []
    for a in range(len(lista)):
        if lista[a][2] == setor:
            del lista[a][2]
            lista2 = lista2 + [lista[a]]
	return lista2