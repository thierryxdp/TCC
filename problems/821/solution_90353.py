def fatorial(num:int)-> int:
    """Recebe um número e calcula seu fatorial"""
    fat=1
    i=1
    while i<=num:
        fat=fat*i
        i=i+1
    return fat