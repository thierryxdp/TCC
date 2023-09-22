# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''
       Dado duas listas: lista1 e lista2 geram uma terceira
       lista que corresponde as lista1 e lista2 intercaladas
       list, list -> list
    '''
    lista3 = [str(lista1[0]) + ',' + str(lista2[0]) + ',' + str(lista1[1]) + ',' + str(lista2[1]) + ',' + str(lista1[2]) + ',' + str(lista2[2])]
    return lista3