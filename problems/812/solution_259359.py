def verifica_caracter(c):
    pontuacoes = ['-',
                    ',',
                    ':',
                    ';',
                    '...',
                    '.',
                    '?',
                    '!'
                    ]
    return ' ' if c in pontuacoes else c
def retira_pontuacao(frase):
    '''Funcao que dada uma frase, retorna a frase onde os caracteres de pontuacao tenham sido substituidos por espaco.'''
    
    	FraseAlterada = str.join(
            '',
            map(verifica_caracter, frase)
        	)
        
    	return FraseAlterada
    	
        return