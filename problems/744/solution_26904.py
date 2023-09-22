# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    posicao = len(s) // 2
    antes = s[:posicao]
    depois = s[posicao:]
    return "#" + antes + "#" + depois + "#"