def retira_pontuacao(frase):
	'''funçao que recebe uma frase e troca sua pontuaçao por espaço;
    str->str'''
    
    
	x = x + str.replace(frase,',',' ')
    x = x + str.replace(frase,'!',' ')
    x = x + str.replace(frase,'?',' ')
    x = x + str.replace(frase,'_',' ')
    x = x + str.replace(frase,'-',' ')
    
    return x