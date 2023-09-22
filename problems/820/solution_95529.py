def posLetra(frase,letra, ocorrencia):
    ''' função que recebe como entrada como entrada uma string, 
    uma letra e a ocorrência dessa letra 
    retorna em qual posição aquela ocorrência da letra
    entrada:str,str,int
    saída:int'''
    posicao=0
    i=0
    if str.count(frase, letra)>=ocorrencia:
        if frase[posicao]==letra:
            while posicao<len(frase):
                posicao=posicao+1
        		i=i+1
    	return i     		
    else:
        return -1