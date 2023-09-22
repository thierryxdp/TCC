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
    y = x//2
    return "#" + y[0] + y[1] + "#" + y[2] + y[3] + "#"