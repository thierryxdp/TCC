def posLetra(string,letra,numero):
    """Retorna a posição da string em que a ocorrencia a letra está.Caso não exista
    ocorrencias da letra pedida a função retorna -1.
    Parametros:
    Entrada: str,str,int
    Saida:int"""
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