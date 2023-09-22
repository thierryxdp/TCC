# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que inseri hashtags no início, meio e fim de um texto de informação "s" de entrada: str -> str'''
    metade = len(s)//2
    return '#' + s[:metade] + '#' + s[metade:] + '#'