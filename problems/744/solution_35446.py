# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    diego = len(s) // 2
    return "#" + s[:diego] + "#" + s[diego:] + "#"