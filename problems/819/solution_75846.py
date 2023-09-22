def filtraMultiplos (lista, numero):
    """Filtra os multiplos do numero na lista
    list, int -> list"""
    
    i = 0
    NovaLista = []
    
    while i < len(lista):
        if lista [i] % numero == 0:
            NovaLista.append(lista[i])
            
        i += 1
    
    return NovaLista