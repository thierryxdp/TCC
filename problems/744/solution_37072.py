# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    i=((len(s))/2)-1
    y=list(s)
    y[i]=('#')
    z="".join(y)
    return ('#'+(z)+'#')