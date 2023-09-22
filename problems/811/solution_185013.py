def colchao(medidas,H,L):
    area_porta = H * L
    a1 = medidas[0] * medidas[1]
    a2 = medidas[0] * medidas[2]
    a3 = medidas[1] * medidas[2]
    if area_porta>=a1 or area_porta>=a2  or area_porta>=a3:
        return True
    else:
        return False