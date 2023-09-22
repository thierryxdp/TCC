# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)/2 != 1:
        meiopar = len(s)//2
        return '#' + str(s[0:meiopar]) + '#' + str(s[meiopar:])
    else:
        meioimpar = (len(s)//2) - 1
        return '#' + str(s[0:meioimpar]) + '#' + str(s[meioimpar+1:])