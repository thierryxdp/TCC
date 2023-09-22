# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    parte_1 = s[0:]
    parte_2 = s[:len(s)]
    return '#' + parte_1 + '#' + parte_2 '#'