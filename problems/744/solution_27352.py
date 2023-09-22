# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Preparação teste"""
    if len(s) == 0:
        return "#" + s + "#"
    elif len(s) == 1:
        return "#" + s + "#"
    elif len(s)%2 == 0:
        return "#" + [:len/2] + "#" + [len/2:] + "#"
    else: "#" + [:len//2] + "#" + [len//2:] + "#"