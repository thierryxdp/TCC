def troca(frase):
    for pontuacao in "--,:;.":
        frase = frase.replace(pontuacao, "")
  	return frase
print (troca("frase"))