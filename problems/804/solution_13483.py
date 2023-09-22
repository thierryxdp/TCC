def filtra_pares(tupla):
    """funcao que dado de entrada um tupla com 4 elementos
    inteiros, retorna uma nova tupla contendo somente os 
    elementos pares da tupla original;
    tuple -> tuple"""
    
    E1 = tupla[0]%2
    E2 = tupla[0]%2
    E3 = tupla[0]%2
    E4 = tupla[0]%2
   
    return tuple(E1 for E1==0)