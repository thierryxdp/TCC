def retira_pontuacao(frase):
    """
    Função que retira qualquer pontuação de uma frase e substitui por um espaço em branco
    str --> str
    """
    
    
    nova_frase=frase.replace('-',' ').replace(':',' ') .replace('.',' ') .replace(',',' ').replace('?',' ') .replace('!',' ') 
	
    return nova_frase