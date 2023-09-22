def inverte(frase):
    '''
    Função que recebe uma frase e a retorna sem pontuação, com 
	letras minúsculas e com a ordem das palavras invertida.
	str -> str'''
    texto = retira_pontuacao(frase).lower()
    texto = texto.split()
    return ' '.join(texto[::-1])