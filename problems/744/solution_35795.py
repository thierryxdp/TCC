# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    pp = s[:len(s)//2]
    sp = s[len(s)//2:]
    s = "#" + pp + "#" + sp + "#"