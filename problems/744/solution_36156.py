# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    n=list(s)
    a=len(n)
    b=(a//2)
    h = list.insert(n,1,"#")
    strh = ",".join(h)
    return h