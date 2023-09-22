def filtraMultiplos(lista,n):
    """analisa se todos os numeros da lista são multiplos de n;
    lista, int -> lista"""
    resultado= []
    parametro = 0
    
    while parametro < len(lista):
        if lista[parametro]%n = 0:
            resultado = resultado + [lista[parametro]]
            parametro = parametro + 1
        else:
            parametro = parametro + 1
    return resultado