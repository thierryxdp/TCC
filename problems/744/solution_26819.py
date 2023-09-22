# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Função que insere uma hashtag no início, meio e fim de uma string s; str -> str'''
    fatiamento1= s[0:len(s)//2]
    fatiamento2= s[len(s)//2:len(s)]
    return '#'+fatiamento1+'#'+fatiamento2+'#'