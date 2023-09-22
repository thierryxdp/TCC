# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Adiciona hashtags no começo, no meio, e no fim da função""""
    return "#" + s[0:len(s)//2] + "#" + s[len(s)//2:] + "#"