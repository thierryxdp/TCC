def retira_pontuacao(frase):
    '''funçao retira todos os caracteres de pontuaçao, os quais sao substituidos por espaços'''
    '''str -> str'''
    
    str.strip(frase, '.')
    str.strip(frase, ',')
    str.strip(frase, '-')
    str.strip(frase, ':')
    str.strip(frase, ';')
    
    f = str.strip(frase, '.')
    
    return f