# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hash(s):
    meio = len(s)//2
    metade_1=s[0:meio]
    metade_2=s[meio:]
    return '#'+metade_1+'#'+metade_2+'#'