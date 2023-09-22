def retira_pontuacao(frase):
    '''
    Função que recebe uma frase e a retorna sem pontuação.
	str -> str
    '''
    texto = frase.replace('!', ' ')
    texto = texto.replace('?', ' ')
    texto = texto.replace('...', ' ')
    texto = texto.replace('.', ' ')
    texto = texto.replace(',', ' ')
    texto = texto.replace('—', ' ')
    texto = texto.replace(':', ' ')
    texto = texto.replace(';', ' ')
    texto = texto.replace('-', ' ')
    return texto

def inverte(frase):
    '''
    Função que recebe uma frase e a retorna sem pontuação, com 
	letras minúsculas e com a ordem das palavras invertida.
	str -> str'''
    texto = retira_pontuacao(frase).lower()
    texto = texto.split()
    return ' '.join(texto[::-1])