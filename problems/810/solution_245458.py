def inverte (frase):
    '''Função que retira a pontuação da frase, inverte o sentido e coloca tudo em letras minúculas;
    str -> str'''
    
     
#primeiro retirar a pontuação:
    
    if '-' in frase:
        var frase1 = str.replace(frase,'-',' ') 
    
    if ',' in frase:
        var frase1 = str.replace(frase,',',' ') 
    
    if ':' in frase:
        var frase1 = str.replace(frase,':',' ') 
    
    if ';' in frase:
        var frase1 = str.replace(frase,';',' ') 
    
    elif '.' in frase:
        var frase1 = str.replace(frase,'.',' ') 
        
    elif '!' in frase:
        var frase1 = str.replace(frase,'!',' ') 
        
    elif '?' in frase:
        var frase1 = str.replace(frase,'?',' ')    
              
# colar a frase em letras minúsculas
	var frase2 = str.lower(frase1) 

#colocar a frase em lista
	var frase3 = str.split(frase2)

#inverter a frase
	var frase4 = str.reverse(frase3)

	return frase4