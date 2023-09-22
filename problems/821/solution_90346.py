def fatorial(num:int)-> int:
    """Recebe um número e calcula seu fatorial"""
    fat=0
    fator=0
    while fat<num:
        fator=fat+1
        fat=fat*fator
    return fator