# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """A função além de unir duas listas intercala elas usando a função Zip"""
    return [*sum(zip(lista1,lista2),())]