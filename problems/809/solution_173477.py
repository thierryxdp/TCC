# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """recebe duas listas 'l1' e 'l2' de tamanho 3 e gera uma lista 'l3' formada intercalando-se os elementos de l1 e l2"""
    l3=l1+l2
    l3[1]=l2[0]
    l3[2]=l1[1]
    l3[3]=l2[1]
    l3[4]=l1[2]
    l3[5]=l2[2]
    l3[6]=l1[3]
    return l3