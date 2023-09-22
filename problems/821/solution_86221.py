def fatorial(num):
    """Retorna o fatorial do número de entrada; int ou float -> int."""
    x = num
    fat = num
    while x>0:
        x = x - 1
        fat = fat * x
    return fat