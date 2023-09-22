# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    sub_str = s[:len(s)//2]
    sub_str2 = s[len(s)//2:]
    return '#' + sub_str + '#' + sub_str2 + '#'