# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a = -1
    b = len(s)//2
    c = len(s) + 1
    d = list(s)
    d[a] = '#"
    d[b] = '#"
    d[c] = '#"
    return "".join(d)