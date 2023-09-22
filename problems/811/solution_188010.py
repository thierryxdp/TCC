def colchao(medidas,H,L):
    medidas = ['A','B','C','H','L']
    if ('A' > 'B'):
        return True
    if ('B' > 'C'):
        return True
    if ('L' > 'H'):
        return True
    else:
        return False