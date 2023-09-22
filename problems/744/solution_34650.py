# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    return "#" + part1(s) + "#" + part2(s) + "#"             
def comp(s):
    return (len(s))/2
def part1 (s):
    return s[0:comp(s)]
def part2 (s):
    return s[comp(s)+1:]