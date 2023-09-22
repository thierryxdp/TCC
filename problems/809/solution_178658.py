# Questao 1
def intercala(lista1, lista2):
    """
Funcao que dadas duas listas de tamanho 3,
retorna uma terceira lista com os elementos
da primeira e segunda listas intercalados
str, str
    """
    return [*sum(zip(lista2,lista1),())]