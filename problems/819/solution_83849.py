def filtraMultiplos(lista,n):
    """Função que dada uma lista e um número, retorna outra
    lista contendo apenas os números que forem divisíveis por
    esse número dado.
    list, int -> list"""
    
    i = 0
    multiplos = []
    
    while i < len(lista):
        
        if lista[i] % n == 0:
            multiplos += lista[i]
        i += 1
        
        return multiplos