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
    frase = str.replace(frase,'-', ' ')
    
    return frase

def inverte(frase):
    '''
    	Função que recebe como parâmetro
        uma frase e retorna essa frase
        sem pontuação, sem letras 
        maiúsculas e com as palavras na 
        ordem inversa
        : param frase: str
        : return: str
    '''
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.strip(frase)
    frase = str.split(frase)
    list.reverse(frase)
    frase = str.join(' ', frase)
    
    return frase