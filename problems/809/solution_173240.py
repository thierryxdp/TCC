# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao que retorna uma terceira lista, com base nos valores da lista1
    intercalados com os valores da lista 2.
    Entrada: list, list;
    Saida: list
    
    Parameters:
    lista1: primeira lista a intercalar
   	lista2: segunda lista a intercalar
    """
    
    Termo_1 = lista1[0]
    Termo_2 = lista2[0]
    Termo_3 = lista1[1]
    Termo_4 = lista2[1]
    Termo_5 = lista1[2]
    Termo_6 = lista2[2]
    
    lista3 = [Termo_1 , Termo_2 , Termo_3 , Termo_4 , Termo_5 , Termo_6]
    
    return lista3