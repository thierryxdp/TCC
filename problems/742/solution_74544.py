# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    part1 = [0:i]
    part2 = s[i+1:len(s)]
    return part1 + x + part2