# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ao receber duas listas contendo 3 números,
    intercala as listas, em uma nova lista.
    list, list -> list"""
    n1 = lista1[:1] # 1º da lista 1
    n2 = lista2[:1] #1º da lista 2
    n3 = lista1[1:2] #2º da lista 1
    n4 = lista2[1:2] #2º da lista 2
    n5 = lista1[2:] #3º da lista 1
    n6 = lista2[2:] #3º da lista2
    return n1 + n2 + n3 + n4 + n5 + n6