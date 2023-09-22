# cria hashtags entre string
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio = len (s) /2
    return s[0] + '#' + s[ 0:meio] + '#' + s[:meio]