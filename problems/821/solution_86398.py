def fatorial(numero:int)->int:
    """Dado um número, retorna o seu fatorial."""
    fat_numero=1
    while numero>1:
        fat_numero=fat_numero*(numero)
        numero=numero-1
    return fat_numero