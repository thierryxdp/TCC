def media_matriz(matriz):
    '''função que dada uma matriz, retorna uma média entre 
    todos os numeros com duas casas decimais de precisão
    list->int '''
	soma = 0
    tamanho = 0
	for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    return soma / tamanho