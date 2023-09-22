def freq_palavras(frase):
	dicio = dict()
      frase_list = frase.split()
      frase_unique = set(frase_list)
      for palavra in frase_unique:
            dicio[palavra] = frase_list.count(“palavra”)
	
		
		return dicio