# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''
     uma funcao que dada duas listas (L1 e L2) de tamanho 3,
     gera uma lista L3 que é formada intercalando os elementos
     da L1 e L2
     :param lista1: list
     :param lista2: list
     :return: list
    '''
     lista3 = lista1 + lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3