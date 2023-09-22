def filtraMultiplos(lista_de_numeros,n):
    """Função que retorna n múltiplos de um valor x inserido."""
    """List, int -> list"""
    i = 0
    nova_lista = []
    
    while i < len(lista_de_numeros):
        if lista_de_numeros[i] % n == 0:
            nova_lista.append(lista_de_numeros[i])
        i = i + 1
    return nova_lista