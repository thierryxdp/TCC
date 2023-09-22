def retira_pontuacao(frase):
    '''
    	Funcao que recebe uma frase e retorna a mesma frase
        com todos os caracteres de pontuacao substituidos por
        espaços
        string -> string
    '''
    a = frase.replace('-', ' ')
	b = frase.replace(',', ' ')
    c = frase.replace(':', ' ')
    d = frase.replace(';', ' ')
    e = frase.replace('.', ' ')
    return frase