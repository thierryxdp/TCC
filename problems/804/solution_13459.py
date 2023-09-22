def filtra_pares(tupla):
    """funcao que dado de entrada um tupla com 4 elementos
    inteiros, retorna uma nova tupla contendo somente os 
    elementos pares da tupla original;
    tuple -> tuple"""
    
    E1 = tupla[0]%2
    E2 = tupla[1]%2
    E3 = tupla[2]%2
    E4 = tupla[3]%2
    
    return tuple((E1 if E1==0),(E2 if E2==0),(E3 if E3==0),(E4 if E4==0))