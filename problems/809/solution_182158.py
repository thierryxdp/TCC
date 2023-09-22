# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    print ('original list1 : ' + str (list1))
    print ('original list2 : ' + str(list2))
    res = list1 + list2
    res [::2] = list1
    res [1::2] + list2
    print ('the interleaved list is :' + str(res))