# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    "Concatena as string informadas e retorna no formato abba"
    textoA = a
    textoB = b
    concat = textoA + textoB + textoB + textoA
    return concat