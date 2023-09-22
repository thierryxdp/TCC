def filtra_pares(elementos):
    '''
    	Funcao que recebe uma tupla com quatro elementos 
        inteiros e retorna uma nova tupla contendo apenas
        os elementos pares da tupla original
        tupla -> tupla
    '''
    a = elementos[0]
    b = elementos[1]
    c = elementos[2]
    d = elementos[3]
    
    if a%2==0:
        return "("a")"
    if b%2==0:
        return b
    if c%2==0:
        return c
    if d%2==0:
        return d
    else:
        return "()"