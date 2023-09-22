def inverte(texto):
    texto= str.replace(texto,'-',' ')
    texto= str.replace(texto,',',' ')
    texto= str.replace(texto,':',' ')
    texto= str.replace(texto,';',' ')
    texto= str.replace(texto,'.',' ')
    texto= str.replace(texto,'?',' ')
    texto= str.replace(texto,'!',' ')
    texto_separado = texto.split()
    tamanho = len(texto_separado)
    contador = 0
    palavra = []
    while contador != tamanho:
	posicao_palavra = tamanho-1
	palavra = texto_separado[posicao_palavra]
	contador = contador + 1
	posicao_palavra = posicao_palavra-1
    return posicao_palavra