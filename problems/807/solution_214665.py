def conta_frases(frase):
   
	'''
      funçao que dada 1 frase retorna a quantidade de palavras nela
      
      Paramentro:
            Entradas:
                frase: str
                    valor da frase fornecida
           	Retorna:
                a quantidade de palavras na frase fornecida
     '''
    frase1 = frase.split()
    return len(frase1)