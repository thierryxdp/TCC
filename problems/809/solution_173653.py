# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Recebe uma lista1 e uma lista2 e retorna uma nova lista formada pelos elementos intercalados das anteriores"""
    return [i for pair in zip(lista1, lista2) for i in pair]