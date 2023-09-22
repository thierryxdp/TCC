def media_matriz(matriz):
    '''função que dada uma matriz, retorna uma média entre 
    todos os numeros com duas casas decimais de precisão
    list->int '''
	soma = 0
    divisao = 0
	for linha in matriz:
        soma += sum(linha)
        divisao += len(linha)
    return round(soma / divisao,2)