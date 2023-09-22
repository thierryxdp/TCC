def fatorial(numero):
    """Recebe um número e retorna seu fatorial.
       int->int
       
       Parameters:
       numero: O número no qual sera calculado o fatorial."""
    i=0
    fat=1
    numero2=numero
    while i<numero:
        fat=fat*numero2
        numero2=numero2-1
        i=i+1
    return fat