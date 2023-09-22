def media_matriz(matiz):
    '''funcao que dada uma matris de 
    numeros inteiros retorna a media de todos os 
    seus numeros com exatos duas casas decimais'''
    med = 0
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
        conta = med/(len(matriz)*len(matriz[0]))
	return round(conta,2)