# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    antes = s[:len(s)//2]
    depois = s[len(s)//2:]
    return "#" + antes + "#" + depois + "#"