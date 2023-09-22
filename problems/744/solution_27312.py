# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Altera uma string inserindo '#' no inicio meio e final dela.
    """
    total=len(s)
    meio=total//2
    return '#'+s[0:meio]+'#'+s[meio:total]+'#'