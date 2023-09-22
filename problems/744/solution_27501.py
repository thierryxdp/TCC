# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    f = ''+ s + ''
    a = 0
    b = len(s)//2 
    c = len(s)
    d = list(s)
    d[a] = '#'
    d[b] = '#' + d[b]
    d[c] = '#'
    return "".join(d)