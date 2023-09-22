# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    	Funçao que recebe uma string e colaco # no começo, meio e final dela
        str -> str
    '''
    return '#' + s[len(s)://2] + '#' + s[len(s)//2:] + '#'