# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Recebe duas listas e junta seus elementos retornando uma lista só.
    list, list -> list"""
    lista3 = [0,0,0,0,0,0]
    lista3[0] = lista1[0]
    lista3[1] = lista2[0]
    lista3[2] = lista1[1]
    lista3[3] = lista2[1]
    lista3[4] = lista1[2]
    lista3[5] = lista2[2]
    return lista3