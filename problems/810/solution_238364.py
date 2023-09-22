#------------EXERCICIO 4-------------

def inverte(texto):
    '''Inverte a ordem das palavras e retira os pontos
       str -> str'''
	
    texto = str.replace(texto, '-', ' ')
    texto = str.replace(texto, ',', ' ')
    texto = str.replace(texto, ':', ' ')
    texto = str.replace(texto, ';', ' ')
    texto = str.replace(texto, '...', ' ')
    texto = str.replace(texto, '!', ' ')
    texto = str.replace(texto, '?', ' ')
    texto = str.replace(texto, '.', ' ')
    
    txtSemPonto = retira_pontuacao(texto)
    listaPalavras = str.split(txtSemPonto)
    
    return str.lower(' '.join(reversed(listaPalavras)))