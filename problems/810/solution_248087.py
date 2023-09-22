def inverte(frase):
    '''
    	Funcao que recebe uma frase e retorna uma outra frase
        que contenha as mesmas palavras da frase de entrada
        na ordem inversa, sem letras maiusculas e sem a 
        pontuacao
        string -> string
    '''
    if '-' in frase:
    	frase = frase.replace('-', ' ')
	if ',' in frase:
        frase = frase.replace(',', ' ')
    if ':' in frase:
        frase = frase.replace(':', ' ')
    if ';' in frase:
        frase = frase.replace(';', ' ')
    if '.' in frase:
       	frase = frase.replace('.', ' ')
    if '?' in frase:
        frase = frase.replace('?', ' ')
    if '!' in frase:
        frase = frase.replace('!', ' ')
    return frase