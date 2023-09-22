def fatorial(numero:int)->int:
    """Dado um número, retorna o seu fatorial."""
    copia_numero=numero
    fat_numero=copia_numero*1
    while numero>=1:
        fat_numero=fat_numero*(numero-1)
        numero=numero-1
    return fat_numero