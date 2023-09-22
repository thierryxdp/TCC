# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """usei o metódo de append pra juntar a lista 1 com a 2"""
    intercalada = []
    for lista1,lista2 in zip(lista1, lista2):
        intercalada.append(lista1)
        intercalada.append(lista2)
    return intercalada