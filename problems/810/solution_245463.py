def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
     
#primeiro retirar a pontuação:
    
    if '-' in frase:
        frase1 = str.replace(frase,'-',' ') 
    
    if ',' in frase:
        frase1 = str.replace(frase,',',' ') 
    
    if ':' in frase:
        frase1 = str.replace(frase,':',' ') 
    
    if ';' in frase:
        frase1 = str.replace(frase,';',' ') 
    
    elif '.' in frase:
        frase1 = str.replace(frase,'.',' ') 
        
    elif '!' in frase:
        frase1 = str.replace(frase,'!',' ') 
        
    elif '?' in frase:
        frase1 = str.replace(frase,'?',' ')
        
    return frase1
              
# colar a frase em letras minúsculas
	frase2 = str.lower(frase1) 

#colocar a frase em lista
	frase3 = frase2.split()

#inverter a frase
	frase4 = str.reverse(frase3)

	return frase4