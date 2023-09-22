# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) % 2 == 0:
        primeira_parte = (len(s) // 2)
    else:
        primeira_parte = (len(s) // 2) +1

    string_saida = '#' + s[0:primeira_parte] + '#' + s[primeira_parte: len(s)] + '#'
    return string_saida