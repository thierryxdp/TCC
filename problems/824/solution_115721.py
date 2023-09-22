def uppCons(frase):
    '''
    funcao que recebe uma frase e converte todas as consoantes em 
    letra maiuscula
    str -> str
    '''
    contador = 0
    frasefinal = ''
    letras = 'bcdfghjklmnopqrstvxwyzç'
    caracter = ''
    
    while contador < len(frase):
         
    	if frase[contador] in letras:
			 caracter = str.upper(frase[contador])
        contador += 1
		frasefinal += caracter
        
        return frasefinal