def retira_pontuacao(frase):
	if '-' in frase:
         frase=str.replace(frase,'-',' ') 
    if ',' in frase:
         frase= str.replace(frase,',',' ') 
    if ':' in frase:
         frase= str.replace(frase,':',' ')
    if '.' in frase:
        return str.replace(frase,'.',' ')