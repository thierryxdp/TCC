def retira_pontuacao(frase):

    '''
      funçao que dada 1 frase retorna ela mesma sem pontuaçao
      
      Paramentro:
            Entradas:
                frase: str
                    valor da frase fornecida
           	Retorna:
                Uma nova frase mas so que sem pontuaçao
	'''
	frase1 = frase.replace('!',' ').replace('.',' ').replace(',',' ').replace(';',' ').replace(':',' ').replace('?',' ').replace('-',' ')
    return frase1