def filtra_pares(lista):
    """função que retorna uma tupla com os elementos pares da tupla de entrada 'lista';
    entrada: tupla(int, int, int, int)
    saída: tupla (int, int, int, int)"""
    e1 = lista[0]
    e2 = lista[1]
    e3 = lista[2]
    e4 = lista[3]
    resultado = ()
    
    if e1%2 == 0:
        resultado = resultado + e1
    if e2%2 == 0:
        resultado = resultado + e2
    if e3%2 == 0:
        resultado = resultado + e3
    if e4%2 == 0:
        resultado = resultado + e4
    return resultado