def media_matriz(matriz):
	"""Calcula e retorna a media de todos os numeros da matriz,com duas
    casas decimais de precisao, sendo a matriz composta de inteiros nao
    vazia; list --> float"""
    media1=0
    media2=0
    for i in matriz:
        for j in i:
            media1=media1+j
        media2=media1/(len(matriz)*len(i))
    return round(media2,2)