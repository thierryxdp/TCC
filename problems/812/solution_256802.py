def retira_pontuacao(frase):
    
    '''Função que irá substituir quaisquer pontuação da frase por um espaço'''
	sinais = '.' and ';' and '!' and '?' and ';' and '/' and '...' and '""' and '(' and ')' and ','  and '[' and ']'
    for sinais in frase:
        return str.replace(frase,sinais,' ')