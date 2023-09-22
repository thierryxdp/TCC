# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    caracter_meio = len(s)//2
    part1 = s[0:caracter_meio]
    part2 = s[caracter_meio:len(s)]
    return '#' + part1 + '#' + part2 + '#'