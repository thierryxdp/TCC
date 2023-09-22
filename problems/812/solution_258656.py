def troca(phrase):
    for pontuacao in "--,:;.":
        phrase = phrase.replace(pontuacao, "")
  	return phrase
print (troca("phrase, teste! estou: testing... this, here?"))