# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ Gera uma nova lista contendo os valores da lista 1 e 2 intercalados.
    	list, list -> list
        
        Parameters:
        lista1: Lista 1
        lista2: Lista 2
        
        Returns:
        Lista com os valores das listas 1 e 2 intercalados
        
        Exemplo: lista1 = [1, 3, 5] e lista2 = [2, 4, 6] gera [1, 2, 3, 4, 5, 6] """
    lista = []
    lista.append(lista1[0])
    lista.append(lista2[0])
    lista.append(lista1[1])
    lista.append(lista2[1])
    lista.append(lista1[2])
    lista.append(lista2[2])
    return lista