def media_matriz(matriz):
    """Dada uma matriz (lista), a função irá somar
    o valor de cada elemento individual e dividir
    pela quantidade total de elementos da matriz.
    Tipo da variável matriz: list
    Tipo da saída: float"""
    soma = 0
    qtd = 0
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            soma = soma + matriz[contador][contagem]
            qtd = qtd + 1
	return round(soma/qtd,2)