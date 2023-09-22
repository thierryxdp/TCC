# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    p1= s[:len(s)//2]
    p2= s[len(s)//2:]
    return '#' + p1 + '#' + p2 + '#'