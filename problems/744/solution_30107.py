# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Função que retorna o string com '#' no começo, meio e final
    str -> str """
   
    return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'