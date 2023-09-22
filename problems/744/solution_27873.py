# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    "adiciona hashtags no inicio, no meio e no fim da função. str -> str"""
    return "#" + s[0:len(s)//2] + "#" + s[len(s)//2:] + "#"