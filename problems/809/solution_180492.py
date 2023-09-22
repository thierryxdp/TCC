# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''
       A função recebe duas listas e retorna as duas listas
       intercaladas em uma só
       list, list -> list
    '''
    lista1[1] = lista2[0]
    lista1[2] = lista2[1]
    lista1[3] = lista2[2]
    return lista1