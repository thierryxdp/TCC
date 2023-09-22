# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Insere # no inicio, no meio e no fim da string
       Entrada: str
       Saida: str
    """
    if 0<=len(s)<=1:
        return '#'+'#'+s[:]+'#'
    if 2<=len(s)<=3:
        return '#'+s[0:1]+'#'+s[1:]+'#'
    if 4<=len(s)<=5:
        return '#'+s[0:2]+'#'+s[2:]+'#'
    if 6<=len(s)<=7:
        return '#'+s[0:3]+'#'+s[3:]+'#'
    if 8<=len(s)<=9:
        return '#'+s[0:4]+'#'+s[4:]+'#'
    if 10<=len(s)<=11:
        return '#'+s[0:5]+'#'+s[5:]+'#'
    if 12<=len(s)<=13:
        return '#'+s[0:6]+'#'+s[6:]+'#'
    if 14<=len(s)<=15:
        return '#'+s[0:7]+'#'+s[7:]+'#'