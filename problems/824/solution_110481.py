def uppCons(frase):
	'''retorna todas as consoantes da frase inserida em letras
    maiusculas
    str -> str'''
    
    i = 0
    
    vogais = 'aeiouáéíóúâêîôûàèìòùãõ'
    vogais_mais = str.upper(vogais)
    vogais_total = vogais + vogais_mais
    
    while i < len(frase):
        if frase[i] not in vogais_total:
            maiuscula = str.upper(frase[i])
            
            str.replace(frase,frase[i],maiuscula)
        
    	i = i + 1
                        
    return frase