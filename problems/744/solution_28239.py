# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
import math
def hashtag(s):
    Jogo_da_velha = '#'
    Qchar = len(s)
    Meiochar = Qchar/2
    Pri_lado = math.floor(Meiochar)
    Seg_lado = math.floor(Meiochar)
    Fim = Jogo_da_velha+s[:Pri_lado]+Jogo_da_velha+s[Seg_lado:]+Jogo_da_velha
    return Fim