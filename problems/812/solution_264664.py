def retira_pontuacao(frase):
    oracao=frase
    if str.find(oracao,'.')>0:
     return str.strip(oracao,'.')
	elif str.find(oracao,',')>0:
     return str.strip(oracao,'.')