def filtraMultiplos (lista,n):
    """Retorna uma lista de números que forem divisíveis pelo
    número n dado;
    list, int -> list"""
    resultado = []
    a = 0 
    while a < len(lista) : 
        if lista[a]%n == 0 : 
            list.append(resultado,lista[a])
        a = a + 1
    
    return resultado