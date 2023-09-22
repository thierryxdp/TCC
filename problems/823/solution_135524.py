def faltante(lista):
    """Retorna qual número inteiro deste intervalo está faltando.
    lista --> int"""
    
    list.sort(lista)
    i = 1
    
    while i < len(lista) + 1:
        if lista[i] + 1 != lista[i+1]:
            return lista[i] + 1
        elif lista[i] - 1 != lista[i-1]:
            return lista_ordem[i] - 1
        i = i + 1