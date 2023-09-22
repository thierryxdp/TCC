def conta_numero(numero,matriz):
    """Dada uma matriz (lista) e um número inteiro, a função
    irá checar quantas vezes o número está presente na matriz
    e irá retornar a quantidade de ocorrências (vezes)
    Tipo da variável numero: int
    Tipo da variável matriz: list
    Tipo da saída: int"""
    vezes = 0
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if matriz[contador][contagem] == numero:
                vezes = vezes + 1
	return vezes