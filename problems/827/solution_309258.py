def qtd_divisores(n):
    '''
    Funcao que recebe um numero inteiro. A funcao retorna quantos divisores esse numero possui
    int -> int
    '''  
    con = 0
    for i in range(1, n+1):
        if n%i == 0:
            con = con + 1
    return con