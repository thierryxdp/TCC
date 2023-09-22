# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna a string 's' com # no início, meio e fim
    	str -> str'''
    return '#' + s[:len(s)/2 + 1] + '#' + s[len(s)/2 + 1:] + '#'