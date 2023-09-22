# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) != 0:
        new = list(s)
        new[0,len(s)//2,-1] = '#' + s[0,len(s)//2,-1]
        return ''.join(new)
    else:
        return s