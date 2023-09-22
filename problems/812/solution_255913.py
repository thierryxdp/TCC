def retira_pontuacao(frase):
    
    nova_frase=frase.replace('-',' ').replace(':',' ') .replace('.',' ') .replace(',',' ').replace('?',' ') .replace('!',' ') 
	
    return nova_frase