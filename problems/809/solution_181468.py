# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que dadas duas listtas l1,l2 de tamanho 3, gera
     uma lista l3 que é formada intercalando os elementos de l1 e l2;
        int,int->int"""
    lista3= lista1+lista2
    lista3[::2]=lista1
    lista3[1::2]=lista2
    return lista3