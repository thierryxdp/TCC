# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    lista = list(a,b)
    lista1 = lista[-1:]
    final = lista+lista1
    ''.join(final)
    return final