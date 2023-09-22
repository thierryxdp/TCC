# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ Essa função, dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2. 
        
        Parameters:
            lista1 = primeira lista a ser inserida. Deve ter len = 3
            lista2 = segunda lista a ser inserida. Deve ter len = 3

        Testes:
            intercala([1, 3, 5], [2, 4, 6]) = [1, 2, 3, 4, 5, 6]
            intercala([0, 7, 5], [2, 6, 7]) = [0, 2, 7, 6, 5, 7]
            intercala([4, 0, 6], [7, 1, 4]) = [4, 7, 0, 1, 6, 4]

        Returns:
            uma lista L3 que é formada intercalando os elementos de L1 e L2.
            list, list --> list
    """
    lista = [lista1[0] lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista