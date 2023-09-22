# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que retorna uma string com '#' no começo,
    meio e, fim dela, dados como entrada uma string 's''''
    
    return '#'+s[0:(len(s)//2)]+'#'+s[(len(s)//2):]+'#'