def retira_pontuacao(frase):
    frase.replace(';',' ')
    frase.replace('—',' ')
   	while '.' in frase is True:
    	frase.replace('.',' ')
   	while ',' in frase is True:
    	frase.replace(',',' ')
    while ':' in frase is True:
    	frase.replace(':',' ')
    
    return frase