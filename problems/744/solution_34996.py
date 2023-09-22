# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    z=len(s)
    if z%2==0:
        m=z//2
        return '#' + s[:m] + '#' + s[m:]+'#'
    else:
        m=(z-1)//2
        return '#' + s[:m] + '#' + s[m:]+'#'