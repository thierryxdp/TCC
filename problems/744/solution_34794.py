# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ponta = "#" + s + "#"
    meio = len(s)//2
    return ponta[:(meio)+1] + "#" + ponta[(meio)+1:]