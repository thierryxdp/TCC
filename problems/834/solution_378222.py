def media_matriz(matriz):
    
    """ Função que retorna a média de todos os números da matriz"""
	soma=0
    for i in matriz:
        for v in i:
            soma = soma+v
            contagem = contagem+1
    return round(soma/contagem,2)