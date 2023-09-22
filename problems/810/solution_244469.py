def retira_pontuacao(frase):
    '''recebe uma frase e retorna a str sem suas
    pontuações ',' '-' '.' ':' ';' uma vez que são 
    substituidas por ' '.
    str -> str'''
    
    frase = frase.replace(',', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace(';', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    
    return frase


def inverte(texto):
    '''recebe uma frase de entrada em str e retorna
    a str sem a pontuação e com as palavras em ordem
    reversa.
    str -> str'''
    
    texto = str(list.reverse(texto))
    
    return texto