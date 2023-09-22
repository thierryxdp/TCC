# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ""
    lim = len(s)
    f = lim/2
    return "#"+s[:f]+"#"+s[f:]+"#"