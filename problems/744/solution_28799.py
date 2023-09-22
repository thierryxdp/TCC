# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que adiciona '#' no início,meio e fim na palavra
    introduzida pelo parametro s
    str->str'''
    num=len(s)//2
    return '#'+s[0:num]+'#'+s[num:]+'#'