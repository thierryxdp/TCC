#quero uma funcao que dada uma frase retorne a frase onde todos os
#caracteres de pontuacao tenham sido substituidas por espaco
def troca(phrase):
    for pontuacao in "-:!,;?.":
        phrase = phrase.replace(pontuacao, "")
  	return phrase