# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    ''' função que dado dus listas de tamanho 3, retorna
    uma lista de tamanho 6, com os elementos da lista 1
    e 2 em ordem crescente. São dado como entrada
    as listas 1 e 2. list->list'''
    L3 = lista1 + lista2
    return sorted(L3)