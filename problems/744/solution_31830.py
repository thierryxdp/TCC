# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)
    sub_s1 = s[0:x]
    sub_s2 = s[x:0]
    return '#' + sub_s1 + '#' + sub_s2 + '#"