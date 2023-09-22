# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
'''
    A função retorna uma lista formada por uma
    intercalação dadas duas outras listas
    (entrada = lista, lista / saída = lista)
    '''
    l3 = lista1 + lista2
    return l3[ : 4 : 3] + l3[1 : 5 : 3] + l3[2 : : 3]