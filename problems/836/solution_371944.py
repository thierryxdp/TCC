def busca(frase, matriz):
    """Dada uma frase que representa um setor e uma matriz com
    informações pessoais, a função irá retornar as informações pessoais
    das pessoas que trabalham naquele setor, com exceção desta informação.
    Tipo da variável frase: str
    Tipo da variável matriz: list
    Tipo da saída: list"""
    lista = []
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if frase in matriz[contador][contagem]:
                lista.append(matriz[contador])
	if len(lista) == 0:
        return []
	if len(lista) == 1:
        lista[0].remove(frase)
        return lista
	if len(lista) == 2:
        lista[0].remove(frase)
        lista[1].remove(frase)
        return lista