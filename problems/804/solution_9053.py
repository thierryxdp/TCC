def filtra_pares(a,b,c,d):
    '''retorna só os númeroa pares dentre os parâmetros na mesma ordem que foram inseridos; int,int,int,int -> int'''
    Elem0 = ()
    Elem1 = ()
    Elem2 = ()
    Elem3 = ()
    
    if a%2 == 0:
    	Elem0 = a,
    if b%2 == 0:
        Elem1 = b,
    if c%2 == 0:
        Elem2 = c,
    if d%2 == 0:
        Elem3 = d,
    return Elem0 + Elem1 + Elem2 + Elem3