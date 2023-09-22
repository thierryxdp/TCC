def posLetra(frase,letra,ocorrencia):
    ''' Dada como entrada uma frase, uma letra e um numero
    que indica a ocorrencia da letra desejada, retorna em que 
    posicao da string aquela ocorrencia da letra esta
    str, str, int -> int'''
    contador = 0
    while contador < len(frase):
        if frase[contador] == letra:
            ocorrencia = ocorrencia - 1
        if ocorrencia == 0:
            return contador
		contador +=1
  	return -1