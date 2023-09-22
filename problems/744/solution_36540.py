# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l = len(s)
    s1 = round(l/2)-1
    s2 = l - s1
    parte_1 = s[0:s1]
    parte_2 = s[s2:l]
    return '#' + str.join('#', (parte_1, parte_2)) + '#'