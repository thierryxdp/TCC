def inverte(frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
#primeiro retirar a pontuação:
    
    if '-' in frase:
        return str.replace(frase,'-',' ') 
    
    if ',' in frase:
        return str.replace(frase,',',' ') 
    
    if ':' in frase:
        return str.replace(frase,':',' ') 
    
    if ';' in frase:
        return str.replace(frase,';',' ') 
    
    elif '.' in frase:
        return str.replace(frase,'.',' ') 
        
    elif '!' in frase:
        return str.replace(frase,'!',' ') 
        
    elif '?' in frase:
        return str.replace(frase,'?',' ')
        
                 
# colar a frase em letras minúsculas
	frase.lower() 

#colocar a frase em lista
	frase.split()

#inverter a frase
	frase.reverse()

	return frase