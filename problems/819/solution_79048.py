def anterior(lista, n):
    
    for i in lista:
        if i % n == 0:
            return True
        else:
            return False
           
def filtraMultiplos(lista, n):
    """Função que, dada uma lista de números e um número qualquer, filtra
    os múltiplos desse número contidos nessa lista.
    list[float], float -> list[float]"""

    return list(filter(anterior,lista))