def fatorial(num:int)-> int:
    """Recebe um número e calcula seu fatorial"""
    fat=0
    while fat<num:
        fat=fat*(fat+1)
    return fat