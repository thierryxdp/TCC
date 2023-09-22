def inverte(frase):
    '''
    Função que recebe uma frase e a retorna sem pontuação, com 
	letras minúsculas e com a ordem das palavras invertida.
	str -> str'''
    texto = tirapontuacao(frase).lower()
    texto = texto.split()
    return texto[::-1]