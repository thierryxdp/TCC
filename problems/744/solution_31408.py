# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    string_tamanho = len(s)
    string_meio = len(s) / 2
    a = s[:1] + '#' + s[:len(s)/2] + '#' + s[len(s):] + '#'
    return a