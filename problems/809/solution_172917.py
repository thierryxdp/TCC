# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    Esta função recebe duas listas, intercala seus elementos e retorna uma lista
    contendo estes elementos intercalados.
    
    Parametros
    ----------
    lista1 (list) : primeira lista
    lista2 (list) : segunda lista
    """
    l = ['', '', '', '', '', '']
    l[0] = lista1[0]
    l[2] = lista1[1]
    l[4] = lista1[2]
    l[1] = lista2[0]
    l[3] = lista2[1]
    l[5] = lista2[2]
    return l