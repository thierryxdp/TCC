def filtra_pares(tupla):
    """Recebe quatro inteiros e retorna apenas os pares.
    int int int int -> int pares"""
    
    lis = []
    tupla = ()
    
    for i in range(len(tupla)):
        if tupla[i] % 2 == 0:
            lis.append(tupla[i])
            
            return tupla(lis)