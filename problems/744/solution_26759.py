# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(a):
    x = '#'
    metade = len(a)//2
    string1 = a[0:metade]
    string2 = a[metade:]
    return x + string1 + x + string2 + x