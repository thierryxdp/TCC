def eh_quadrada(matriz):
    """Dada uma matriz, a função retorna se essa matriz é
    quadrada ou não. Uma matriz quadrada possui o mesmo numero 
    de colunas e linhas.
       A matriz deve ser escrita entre colchetes[], com cada linha
    dentro de um colchetes também;
       matriz(lista de listas) --> bool"""
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False