# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Esta e a funcao que dadas duas listas l1 e l2 
    de tamanho 3, geram uma lista l3 que é formada 
    intercalando os elementos de l1 e l2'''
    a = [*sum(zip(lista1,lista2),())]
    return a