def posLetra(frase,letra, ocorrencia):
    ''' função que recebe como entrada como entrada uma string, uma letra e a ocorrência dessa letra 
   retorna em qual posição aquela ocorrência da letra
  entrada:str,str,int
  saída:int'''
	posicao=0
	i=0
	while posicao<len(frase):
    	if str.count(frase, letra)>=ocorrencia and frase[posicao]==letra:
        	i=posicao
    else:
        i=-1
    	posicao=posicao+1
    return i