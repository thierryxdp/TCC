def retira_pontuacao(frase):
	'''funçao que recebe uma frase e troca sua pontuaçao por espaço;
    str->str'''
    
    
	x = str.replace(frase,',',' ')
    x = str.replace(frase,'!',' ')
    x = str.replace(frase,'?',' ')
    x = str.replace(frase,'_',' ')
    x = str.replace(frase,'-',' ')
    
    return x