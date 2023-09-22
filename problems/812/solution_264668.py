def retira_pontuacao(frase):
    oracao=frase
    if str.find(oracao,'.')>0:
     return str.strip(oracao,'.')
	  if str.find(oracao,',')>0:
       return str.strip(oracao,'.')