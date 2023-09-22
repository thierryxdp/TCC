# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Introduz um # no início, meio e fim de uma string.
    entrada:str
    saida:str
    """
    return '#' + str(s[0:int(len(s)/2)]) + '#' + str(s[int(len(s)/2):]) + '#'