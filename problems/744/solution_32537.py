# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    s = s
    s[0:4]
    s[4:len(s)]
    s[4:(len(s)//2)]
    return '#' + s[0:4] + '#' + s[4:(len(s)//2)] + '#'