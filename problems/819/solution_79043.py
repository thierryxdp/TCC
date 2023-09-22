def anterior(lista, n):
    
    final = []
    
    for i in lista:
        if i % n == 0:
            list.append(final, i)
            
    return final

def filtraMultiplos(lista, n):
    """Função que, dada uma lista de números e um número qualquer, filtra
    os múltiplos desse número contidos nessa lista.
    list[float], float -> list[float]"""
    
    resultado = (filter(anterior(lista, n),lista))
    
    return resultado