# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Calcula e retorna uma terceira lista com intercalação de 2 outras listas. list, list -> list"""
    l3 = lista1[0]
    l3 += lista2[0]
    l3 += lista1[1]
    l3 += lista2[1]
    l3 += lista1[2]
    l3 += lista2[2]
    return l3