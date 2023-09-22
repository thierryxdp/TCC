# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    t= len(s)
    return '#' + s[0:int(t/2)] + '#' + s[int(t/2):int(t)] + '#'