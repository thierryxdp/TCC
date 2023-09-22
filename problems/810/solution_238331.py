#------------EXERCICIO 4-------------

def retira_pontuacao(texto):
    '''Substitui todos os pontos por espaço
       str -> str'''
    
    texto = str.replace(texto, '-', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, '...', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '?', ' ')
    texto = str.replace(texto, '.', ' ')

    return texto

def inverte(texto):
    '''Inverte a ordem das palavras e retira os pontos
       str -> str'''

    txtSemPonto = retira_pontuacao(texto)
    listaPalavras = str.split(txtSemPonto)
    
    return ' '.join(reversed(listaPalavras))