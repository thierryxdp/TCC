def soma_h(H):
    '''Função que retorne o valor com N termos, int -> float'''
    somatorio = 0
    for x range(1, H):
        if H//x:
            somatorio = somatorio + H
    return round(somatorio, 2)