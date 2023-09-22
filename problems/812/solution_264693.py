def retira_pontuacao(frase):
    oracao=frase
    if str.find(frase,'.')>0:
     return str.replace(frase,'.',' ')
	if str.find(frase,',')>0:
     return str.strip(frase,',')