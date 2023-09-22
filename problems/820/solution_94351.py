def posLetra(string,letra,numero):
    posicao=0
    ocorrencia=0
    while posicao<len(string):
        if string[posicao]==letra and ocorrencia==numero-1:
        	return posicao
        elif string[posicao]==letra:
    		posicao=posicao+1
        	ocorrencia=ocorrencia+1
        else:
            posicao=posicao+1
  		return -1