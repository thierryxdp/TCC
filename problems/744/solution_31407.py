# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    string_tamanho = len(s)
    a = s[:1] + '#' + s[:string_tamanho/2] + '#' + s[string_tamanho:] + '#'
    return a