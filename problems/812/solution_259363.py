def verificaCaracter(c):
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
    'Funcao que dada uma frase, retorna a frase onde os caracteres de pontuacao tenham sido substituidos por espaco.'
    
    	FraseAlterada = str.join('',map(verificaCaracter, frase))
        
    	return FraseAlterada
    	
        return