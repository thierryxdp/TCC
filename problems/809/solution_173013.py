# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """essa funçao retorna uma nova lista intercalando lista1 e 2"""
    l3=lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]
    return l3