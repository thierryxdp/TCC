def retira_pontuacao(frase):
	'''funçao que recebe uma frase e troca sua pontuaçao por espaço;
    str->str'''
    x ='' 
    
	
    x =  str.replace(frase,'!',' ')
    x =  str.replace(x,'?',' ')
    x =  str.replace(x,'_',' ')
    x =  str.replace(x,'-',' ')
    x =  str.replace(x,'.',' ')
    x =  str.replace(x,',',' ')
    return x



def inverte(frase):
	'''funçao que recebe uma frase e retorna a ordem das palavras ao contrario;
    str->str'''
    x= retira_pontuacao(frase)
    
    numero = str.split(x)
    
    
    
    return numero[-1]