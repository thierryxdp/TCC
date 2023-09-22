# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que insere o caractere '#' no início, meio e final de uma string s'''
    s=str(s)
    metade=len(s)//2
    nova_string: '#'+s[0:metade]+'#'+s[metade:]+'#'
        return nova_string