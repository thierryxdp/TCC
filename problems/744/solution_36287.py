# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ""
    lim = len(s)
    v = lim/2 
    a = lim%1
    if lim == (v):
        return "#"+(s[0:v])+"#"(s[v:])+"#"