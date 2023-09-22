def filtraMultiplos(lista,n):
    """Dada uma lista numérica e um número retorna todos aqueles divisíveis por este número.
       list, int -> list"""
    
    posicao = 0
    resultado = []
    
    while posicao < len(lista):
        if lista[posicao] % 2 == 0:
            resultado = resultado + [lista[posicao]]
            return resultado