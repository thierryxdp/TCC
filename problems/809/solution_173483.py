# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """recebe duas listas 'l1' e 'l2' de tamanho 3 e gera uma lista 'l3' formada intercalando-se os elementos de l1 e l2"""
    
    l3=lista1+lista2
    l3[1]=lista2[0]
    l3[2]=lista1[1]
    l3[3]=lista2[1]
    l3[4]=lista1[2]
    l3[5]=lista2[2]
    return l3