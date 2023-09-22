def posLetra(frase, letra, numero):
    '''retorna o index da ocorrencia da letra desejada em uma frase
    str, str, int -> int'''
    ultimaOcorrencia = 0
    index = 0
    while ultimaOcorrencia != numero:
       	index = frase.find(letra, index)
        if(index == -1):
            return -1
        else:
        	ultimaOcorrencia += 1
            
            
	return index