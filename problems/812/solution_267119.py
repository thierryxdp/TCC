def retira_pontuacao(x):
  	def espaco_frase(x):
    frase=x
    frase.replace('.',' ')
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace('—',' ')
    return frase