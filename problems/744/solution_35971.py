# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s=str(s)
    p=len(s)
    return "#"+ s[0:p//2] + "#" + s[p//2:-1]+ "#"