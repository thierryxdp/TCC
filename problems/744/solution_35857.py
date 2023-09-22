# cria hashtags entre string
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio = math.ceil(len (s) /2)
    return  '#' + s[0:meio] + '#' + s[meio:] + '#'