def fatorial (numero):
    """Função que, dado um número, calcular o fatorial.
    Entrada: int.
    Saída: int."""
    
    i=0
    fatorial = ''
    
    while i <= numero:
        fatorial = numero * (numero-i)
        i = i+1
    return fatorial