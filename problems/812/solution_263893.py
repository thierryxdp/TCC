def retira_pontuacao(frase):
    '''
    	Funcao que recebe uma frase e retorna a mesma frase
        com todos os caracteres de pontuacao substituidos por
        espaços
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
    return frase