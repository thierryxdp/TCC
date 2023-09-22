# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l=len(s)
    sub_s1 = s[0:l//2]
    sub_s2 = s[l//2:]

    return '#'+ sub_s1 + '#' + sub_s2 + '#'