# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    quant = len(s)
    quant2 = len(s)/2
    return '#' + s[quant] + '#' + s[quant2] + '#'