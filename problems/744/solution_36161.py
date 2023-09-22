# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    n=list(s)
    a=len(n)
    b=(a//2)
    list.insert(n,a,"#")
    list.insert(n,b,"#")
    list.insert(n,0,"#")
    strn = ''.join(n)
    return strn