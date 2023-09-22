#Questao 1
def intercala(lista1, lista2):
    """
Funcao que dadas duas listas de tamanho 3,
retorna uma terceira lista com os elementos
da primeira e segunda listas intercalados.
list, list
    """
    return [*sum(zip(lista1,lista2),())]