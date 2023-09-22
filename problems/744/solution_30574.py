# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe um str e insira "#" no ínicio, no meio e no
    final dela.
    str->str"""
    q = len(s)
    return "#" + s[:(q//2)] + "#" + s[(q//2):] + "#"