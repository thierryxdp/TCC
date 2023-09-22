def maiores(int_Lista, int_Num):
    """Funcao que recebe uma lista, e retorna essa lista apenas
    com os numeros que sejam maiores que um inteiro definido.
    Entrada: list, int;
    Saída: list;
    
    Parameters:
    int_Lista: Lista de numeros inteiros a ser modificada:
    inst_Num: numero inteiro
    """
    int_Lista.append(int_Num)
    int_Lista.sort()
    posicao = int_Lista.index(int_Num)
    
    return int_Lista[posicao + 1:]