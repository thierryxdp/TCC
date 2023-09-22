def freq_palavras(frase:str)->str: 
    '''Receve uma string (frase), e retorna um dicionario
    em que cada palavra da strinf é uma chave que tem como 
    valor o número de vezes que ela aparece.'''
  #Separa cada item da frase em uma lista
  	frase = frase.split()
  #Cria um dicionário
  	dicionario = {}
  #Gera uma chave pra cada palavra
  	for palavra in frase:
    #define as chaves como 0
    	dicionario[palavra] = 0
  #Soma 1 ao valor da chave a cada vez que aparece a palavra
  	for palavra in frase:
    	dicionario[palavra] +=1
      
  	return dicionario