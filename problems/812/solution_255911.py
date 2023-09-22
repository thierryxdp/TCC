def retira_pontuacao(frase):
    
    nova_frase=frase.replace('_',' ').replace(':',' ') .replace('.',' ') .replace(',',' ') .replace('!',' ') 
	
    return nova_frase