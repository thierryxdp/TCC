# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l = len(s)//2
    s_part1 = s[0:l]
    s_part2 = s[l:len(s)]
    
    return s_part2