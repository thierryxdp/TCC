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
    
    return frase