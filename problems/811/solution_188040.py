def colchao(medidas,H,L):
    medidas = ['A', 'B', 'C', 'H', 'L']
    if('A' >= 'B')or('B' >= 'C')or('L' >= 'H'):
        return True
    else:
        return False