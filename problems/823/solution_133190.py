def faltante(lista):
    """Retorna qual número inteiro deste intervalo está faltando.
    lista --> int"""
    
    lista_crescente = list.sort(lista)
    i = 1
    
    while i < len(lista_crescente):
        if lista_crescente[i] + 1 != lista_crescente[i+1]:
            return lista_crescente[i] + 1
        elif lista_crescente[i] - 1 != lista_crescente[i-1]:
            return lista_crescente[i] - 1
        i = i + 1