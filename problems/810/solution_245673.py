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

def quant_palavras(frase):
    """funçao que recebe uma frase e retorna o numero de palavras;
    str->int"""
    
    numero = str.split(frase,' ',0)
    
    return len(numero)

def inverte(frase):
	'''funçao que recebe uma frase e retorna a ordem das palavras ao contrario;
    str->str'''
    retira_pontuacao(frase)
    quant_palavras(frase)
    
    return retira_pontuacao(frase) , quant_palavras(frase)