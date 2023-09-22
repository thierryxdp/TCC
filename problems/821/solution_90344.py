def fatorial(num:int)-> int:
    """Recebe um número e calcula seu fatorial"""
    fat=0
    fator=0
    while fat<num:
        fat+=1
        fator=fator*fat
    return fator