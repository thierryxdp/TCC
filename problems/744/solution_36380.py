# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a=len(s)
    b=a/2
    s=list(s)
    s.append("#")
    s.insert(0, "#")
    s.insert(b+1, "#")
    s="".join(s)
    return s