# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s)/2 != 1:
        meiopar = len(s)/2
        return str('#') + str(s[0:meiopar]) + str('#') + str(s[meiopar+1:])
    else:
        meioimpar = (len(s)/2) - 1
        return str('#')