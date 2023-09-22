def faltante(lista):
    """Retorna qual número inteiro deste intervalo está faltando.
    lista --> int"""
    
    lista_ordem = list.sort(lista)
    i = 1
    
    while i < len(lista_ordem):
        if lista_ordem[i] + 1 != lista_ordem[i+1]:
            return lista_ordem[i] + 1
        elif lista_ordem[i] - 1 != lista_ordem[i-1]:
            return lista_ordem[i] - 1
        i = i + 1