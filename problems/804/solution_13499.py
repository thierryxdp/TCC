def filtra_pares (a,b,c,d):
    '''funcao que retorna uma tupla apenas com os elementos pares da tupla dada
    tuple(int) -> tuple(int)'''
    modulo_a = a%2
    modulo_b = b%2
    modulo_c = c%2
    modulo_d = d%2
    
    if modulo_a==0 and modulo_b==0 and modulo_c==0 and modulo_d==0:
        return (a,b,c,d)