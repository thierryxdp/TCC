def eh_quadrada (matriz):
    for l in matriz:
        for c in l:
            if c == l:
                matriz = True
            else:
                return False