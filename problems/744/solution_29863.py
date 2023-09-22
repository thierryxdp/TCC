# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(x):
    """Retorna s com hashtag antes, no meio e depois
    str -> str"""
    if len(x) == 1:
        return '#' + '#' + str(x) + '#'
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
    elif len(x) == 7:
        return '#' + str(x[0:3]) + '#' + str(x[3:]) + '#'
    elif len(x) == 8:
        return '#' + str(x[0:4]) + '#' + str(x[4:]) + '#'
    elif len(x) == 9:
        return '#' + str(x[0:4]) + '#' + str(x[4:]) + '#'
    elif len(x) == 10:
        return '#' + str(x[0:5]) + '#' + str(x[5:]) + '#'
    elif len(x) == 11:
        return '#' + str(x[0:5]) + '#' + str(x[5:]) + '#'
    elif len(x) == 12:
        return '#' + str(x[0:6]) + '#' + str(x[6:]) + '#'
    elif len(x) == 13:
        return '#' + str(x[0:6]) + '#' + str(x[6:]) + '#'
    elif len(x) == 14:
        return '#' + str(x[0:7]) + '#' + str(x[7:]) + '#'
    elif x == '':
        return '###'