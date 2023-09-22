# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
# Hashtag
def hashtag(s):
    """recebe uma string, encontra seu meio e coloca uma hashtag no seu inicio meio e fim
    str -> str"""
    l = len(s)
    return "#" + s[0:l//2] + "#" + s[l//2:] + "#"