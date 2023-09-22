def fatorial(n):
    """Funçao que calcule o fatorial do número n; int-> int"""
    i=0
    contador=1
    while contador <= n:
        i=i*contador
        contador= contador+1
    return i