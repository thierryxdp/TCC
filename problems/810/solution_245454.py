def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
     
#primeiro retirar a pontuação:
    
    if '-' in frase:
        frase = str.replace(frase,'-',' ') 
    
    if ',' in frase:
        frase = str.replace(frase,',',' ') 
    
    if ':' in frase:
        frase = str.replace(frase,':',' ') 
    
    if ';' in frase:
        frase = str.replace(frase,';',' ') 
    
    elif '.' in frase:
        frase = str.replace(frase,'.',' ') 
        
    elif '!' in frase:
        frase = str.replace(frase,'!',' ') 
        
    elif '?' in frase:
        frase = str.replace(frase,'?',' ')    
              
# colar a frase em letras minúsculas
	frase2 = str.lower(frase) 

#colocar a frase em lista
	frase3 = str.split(frase2)

#inverter a frase
	frase4 = str.reverse(frase3)

	return frase4