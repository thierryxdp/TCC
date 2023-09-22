def intercala(lista1, lista2):
    """Função que dadas duas listas 1 e 2 de tamanho 3 como entrada,
    gera uma lista que é formada intercalando os elementos
    das listas 1 e 2; lista, lista -> lista"""

    listaA1 = lista1[0]
    listaA2 = lista1[1]
    listaA3 = lista1[2]

    listaB1 = lista2[0]
    listaB2 = lista2[1]
    listaB3 = lista2[2]

    return [listaA1,listaB1,listaA2,listaB2,listaA3,listaB3]