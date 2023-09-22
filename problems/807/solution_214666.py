def conta_frases(frase):
    '''
      funçao que dada uma frase retorna a quantidade de palavras com caracteres especiais
      
      Paramentro:
            Entradas:
                frase: str
                    valor da frase fornecidao
           	Retorna:
                    Um int que representa a quantidade de palavras que contem caracteres especias
    '''
	return frase.count('.',',','!','?',';',':')