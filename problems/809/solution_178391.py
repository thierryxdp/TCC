# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    ''' Essa função recebe duas listas e retorna uma nova com os elemenos das outras intercalado
    list, list --> list'''
    lista = []
    for i in range(0, 3):
        lista = lista + [lista1[i]] + [lista2[i]]
    return lista