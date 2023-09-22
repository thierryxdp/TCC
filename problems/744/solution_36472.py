# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    a = len (s)% 2
    if a == 0:
        t = len (s) + 2
        d = round (t/2)
        return '#' + str (s[0:d -1])+ '#'+ str(s[d-1:])+'#'
    else:
        t = len (s) + 1
        d = round (t/2)
        return '#' + str (s[0:d-]) + '#' + str(s[d-1:])+'#'