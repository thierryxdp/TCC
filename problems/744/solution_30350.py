# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    palavra = str(s)
    metade = len(palavra)//2
    return '#' + palavra[0: metade] + '#' + palavra[metade:] + '#'