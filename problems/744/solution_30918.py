# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    quantidade_caracteres = len(s)
    metade_das_quantidades = int(x/2)
    return "#" + s[0:metade_das_quantidades] + "#" + s[metade_das_quantidades:] + "#"