# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que recebe uma string s, eretorna
    essa string com o caracter # no inicio, meio e 
    fim dessa string'''
    meio = int(len(s)/2)
    new = '#'+s[:meio]+'#'+s[meio:]+'#'
    return str(new)