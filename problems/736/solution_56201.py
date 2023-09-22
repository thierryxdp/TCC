# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    ''' retorna a concatenaçao do tipo abba das strings a,b.
    str,str->str'''
    x=[a,b]
    return x[0]+x[-1]+x[-1]+x[0]