def posLetra(frase, letra, ind):
    indice = 0
    p = str.find(frase, letra)
    while indice < ind - 1:
        if letra in palavra:
            p = str.find(fase, letra, p+1)
		indice += 1
  	return p