# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l=list(s)
    n=len(l)
    m=(n//2)+1
    h = ("#",l[m:m+1],"#",l[m+1:n],"#")
    strh = "".join(h)
    return strh