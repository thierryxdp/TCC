# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l=len(s)
    r=list(s)
    d=int(l/2)
    return "#"+s[0:d]+"#"+s[d:]+"#"