#------------EXERCICIO 4-------------

def inverte(texto):
    '''Inverte a ordem das palavras e retira os pontos
       str -> str'''

    txtSemPonto = retira_pontuacao(texto)
    listaPalavras = str.split(txtSemPonto)
    
    return ' '.join(reversed(listaPalavras))