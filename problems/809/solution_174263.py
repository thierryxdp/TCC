def intercala(lista1, lista2):
    """funçao que recebe duas listas de tamanho 3 e intercala seus elementos
    entrada: list [int, int, int], list [int, int, int];
    saida: list [int,int,int,int,int,int]."""
    
    a = lista1
    b = lista2
    
    return [a[0], b[0], a[1], b[1], a[2], b[2]]