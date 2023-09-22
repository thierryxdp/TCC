# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Dadas as listas 1 e 2 a função retorna uma terceira lista, que é 
       formada pela intercalação das duas listas anteriores.
       list, list -> list
       parametros:
       lista1 : lista a ser digitada
       lista2 : lista a ser digitada'''
    a = list(lista1)
    b = list(lista2)
    return [a[0], b[0], a[1], b[1], a[2], b[2]]