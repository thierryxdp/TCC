# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    lista_1 = (lista1,)
    lista_2 = (lista2,)
    inter0 = lista_1 [0]+lista_2 [0]
    inter1 = lista_1 [1]+lista_2 [1]
    inter2 = lista_1 [2]+lista_2 [2]
    return {inter0,inter1,inter2}