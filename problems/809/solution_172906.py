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
    return sorted(lista1+lista2)