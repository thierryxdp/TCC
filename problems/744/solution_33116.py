# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    	Funcao que recebe uma string (s) e insere o caractere "#" no
        inicio, no meio e no final dela.
        Parametros: (s) str.
        Return: str.
	'''
    
    return '#' + s[:len(s)//2] + '#' + s[(len(s)//2):] + '#'