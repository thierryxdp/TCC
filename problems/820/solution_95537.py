def posLetra(frase,letra, ocorrencia):
    ''' função que recebe como entrada como entrada uma string, 
    uma letra e a ocorrência dessa letra 
    retorna em qual posição aquela ocorrência da letra
    entrada:str,str,int
    saída:int'''
    i=0
    posicao=0
	while posicao<len(frase):
        if str.count(frase, letra)>=ocorrencia: