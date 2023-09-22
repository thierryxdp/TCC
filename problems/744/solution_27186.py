# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """calculo e retorno de uma funcao que tenha o '#'no inicio,meio e fim"""
    b=len(s)//2
    a='#'+s[:b]+'#'+s[b+1:]+'#'