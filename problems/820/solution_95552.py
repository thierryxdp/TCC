def posLetra(frase, letra, ocorrencia ):
    ''' função que recebe como entrada como entrada uma string, 
    uma letra e a ocorrência dessa letra 
    retorna em qual posição aquela ocorrência da letra
    entrada:str,str,int
    saída:int'''
  	if str.count(frase, letra) >= ocorrencia:
        i = 0
     	contagem = 0
    while(contagem < ocorrencia) :
         if frase[i] == letra:
            contagem = contagem + 1
         	i = i + 1
        return i
  else:
        return - 1