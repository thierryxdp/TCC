def posLetra(frase:str,letra:str,ocorrencia:int)->int:
    '''retorna a posição de uma determinada letra, 
    dada a sua ocorrência, caso não haja a ocorrência 
    da quantidade de letras, o valor retornado será -1'''
    i=0
    contador = 0
    while i < len(frase):
        if letra == frase[i]:
            contador += 1
		if contador == ocorrencia:
            return i
        i += 1
	return -1