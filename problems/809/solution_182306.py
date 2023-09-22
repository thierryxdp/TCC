# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    test_list1 = lista1 
    test_list2 = lista2
    lista_interc = test_list1 + test_list2 
    lista_interc[::2] = test_list1 
    lista_interc[1::2] = test_list2
    return lista_interc