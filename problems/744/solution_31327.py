# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s=list(s)
    if len(s)%2==0:
        s.insert(0,"#")
        s.insert(-1,"#")
        return s