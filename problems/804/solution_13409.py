def filtra_pares(tupla):
    """funcao que dado de entrada um tupla com 4 elementos
    inteiros, retorna uma nova tupla contendo somente os 
    elementos pares da tupla original;
    tuple -> tuple"""
    
    E1 = tupla[0]
    E2 = tupla[1]
    E3 = tupla[2]
    E4 = tupla[3]
    
    if E1%2==0 and E2%2==0 and E3%2==0 and E4%2==0:
        return tupla