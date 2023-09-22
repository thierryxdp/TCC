# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return "#" + s[0:(comp(s))/2] + "#" + s[((comp(s))/2)+1:] + "#"
def comp(s):
    return len(s)