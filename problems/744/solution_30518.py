# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
        Recebe uma string e insere o '#' no começo, meio e fim dela.
        str -> str
    '''
    cont = len(s)
    p1 = '#' + s[0]
    p2 = int(len(s) / 2)
    p3 = s[-1] + '#'
    return p1 + s[1:p2] + '#' + s[p2:-1] + p3