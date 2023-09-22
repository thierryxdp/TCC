# Retorna uma string com "#" no seu início, meio e fim
# str-> str
def hashtag(s):
    ponta = "#" + s + "#"
    meio = len(s)//2
    return ponta[:(meio)+1] + "#" + ponta[(meio)+1:]