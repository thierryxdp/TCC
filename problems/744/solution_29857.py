# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna s com hashtag antes, no meio e depois
    str -> str"""
    if len(x) == 1:
        return '#' + str(x) + '#' + str(x) + '#'
    elif len(x) == 2:
        return '#' + str(x[:1]) + '#' + str(x[-1:]) + '#'
    elif len(x) == 3:
        return '#' + str(x[0:1]) + '#' + str(x[1:]) + '#'
    elif len(x) == 4:
        return '#' + str(x[0:2]) + '#' + str(x[2:]) + '#'
    elif len(x) == 5:
        return '#' + str(x[0:2]) + '#' + str(x[2:]) + '#'
    elif len(x) == 6:
        return '#' + str(x[0:3]) + '#' + str(x[3:]) + '#'