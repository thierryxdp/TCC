def filtra_pares(tupla):
    """Funcao que recebe uma tupla com quatro inteiros
    e retorna uma nova tupla contendo apenas elementos pares da tupla original,
    na mesma ordem em que se encontravam.
    tuple(int, int, int, int) -> tuple"""
    
    nova_tupla = ()
    
    if tupla[0] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[0], )

    if tupla[1] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[1], )

    if tupla[2] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[2], )

    if tupla[3] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[3], )
        
    return nova_tupla