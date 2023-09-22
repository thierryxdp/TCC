def retira_pontuacao(frase):
    '''
    	Função que recebe uma frase como
        entrada e retorna essa frase com
        todos os seus caracteres de 
        pontuação substituídos por espaço
        : param frase: str
        : return: str
    '''
    frase = str.replace(frase,'–', ' ')
    frase = str.replace(frase,',', ' ')
    frase = str.replace(frase,':', ' ')
    frase = str.replace(frase,';', ' ')
    frase = str.replace(frase,'...', ' ')
    frase = str.replace(frase,'.', ' ')
    frase = str.replace(frase,'!', ' ')
    frase = str.replace(frase,'?', ' ')
    
    return frase