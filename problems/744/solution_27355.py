# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Preparação teste"""
    if len(s) == 0:
        return "##"
    elif len(s) == 1:
        return "#" + s + "#"
    elif len(s)%2 == 0:
        return "#" + s[0:int(len(s)/2)] + "#" + s[int(len(s)/2):] + "#"
    elif len(s)%2 > 0 and not == 1 or 0:
        return "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"