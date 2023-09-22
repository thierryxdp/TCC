def uppCons(frase):
    '''
    funcao que recebe uma frase e converte todas as consoantes em 
    letra maiuscula
    str -> str
    '''
    contador = 0
    frasefinal = ''
    letras = 'bcdfghjklmnopqrstvxwyzç'
    while contador < len(frase):
          caracter = frase[contador]
            
    	if caracter in letras:
			caracter = str.upper(caracter)
		frasefinal = frasefinal + caracter
        contador = contador + 1
        return frasefinal