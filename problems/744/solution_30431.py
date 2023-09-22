# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Funcão que, dada um string, retorna a mesma string
    com o caracter '#' no ínicio, meio e fim dela.
    str -> str"""
    return '#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'

#casos de teste
#hashtag('casa') == '#ca#sa#'
#hashtag('casas') == '#ca#sas#'
#hashtag('paralelepipedo') == '#paralel#epipedo#'
#hashtag('paralelepipedos') == '#paralel#epipedos#'