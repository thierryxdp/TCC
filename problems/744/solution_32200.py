# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    	Funcao que recebe uma string e recebe "#" no inicio,
        no meio e no final dela
        str -> str
    '''
    x = len(s)
    return "#" + s[0] + s[1] + "#" + s[2] + s[3] + "#"