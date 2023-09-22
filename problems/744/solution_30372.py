# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)//2
    new_s = "#" + s[:x] + "#" + s[x:] + "#"
    return new_s