# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    list,list->list
    :param lista1: Uma lista
    :param lista2: Uma lista
    :return: A intercala as duas listas
    """

    intercalada = []
    for a,b in zip(lista1,lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada