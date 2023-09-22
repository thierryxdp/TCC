def fatorial(num):
    """Esta função dado um número, calcula o fatorial deste número."""
    fat = num
    while num > 1:
        fat = fat * (num - 1)
        num -= 1
    return fat