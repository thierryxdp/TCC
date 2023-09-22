# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
   '''
        Recebe uma string e insere o '#' no começo, meio e fim dela.
        str -> str
    '''
    if len(s) > 0:
        cont = len(s)
        p2 = int(len(s) / 2)
        p3 = s[-1]
        return '#' + s[0:p2] + '#' + s[p2:-1] + p3 + '#'
    else:
        return '#' + '#' + '#'