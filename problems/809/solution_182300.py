# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    test_list1 = lista1 
    test_list2 = lista2 
    print ("Original list 1 : " + str(test_list1)) 
    print ("Original list 2 : " + str(test_list2)) 
    res = test_list1 + test_list2 
    res[::2] = test_list1 
    res[1::2] = test_list2 
    print ("The interleaved list is : " + str(res))