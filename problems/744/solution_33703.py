# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    função que recebe uma string e insere o caractere '#' no início, no meio e no final dela
    '''
    import math
    a = len(s)
    b = math.floor(a/2)
	if len(s)%2 == 0:
        return '#' + s[:b] + '#' + s[b:a] + '#'
    else:
        return '#' + s[:b] + '#' + s[b:a] + '#''