def inverte(frase):
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
        
                 
# colar a frase em letras minúsculas
	frase1 = frase.lower() 

#colocar a frase em lista
	frase1 = frase.split()

#inverter a frase
	frase1 = frase.reverse()

	return frase1