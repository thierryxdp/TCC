# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dados 2 lista gera uma terceira lista com os elementos das 2 listas intercalados"""
    lista3 = [1,2,3,4,5,6]
    lista3[0] = lista1[0]
    lista3[1] = lista2[0]
    lista3[2] = lista1[1]
    lista3[3] = lista2[1]
    lista3[4] = lista1[2]
    lista3[5] = lista2[2]
    return lista3