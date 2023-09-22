# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca # no inicio, meio e fo=inal do string
       Entrada: str
       Saida: str
    """
    if 7<=len(s)<= 8:
        return '#'+s[0:4]+'#'+s[4:]+'#'
    if 0<=len(s)<=3:
        return '#' + s[0:1]+'#'+s[1:]+'#'
    if 5<=len(s)<=6:
        return '#' + s[0:3]+'#'+s[3:]+'#'
    if 9<=len(s)<=10:
        return '#' + s[0:5]+'#'+s[5:]+'#'
     if 11<=len(s)<=12:
        return '#' + s[0:6]+'#'+s[6:]+'#'