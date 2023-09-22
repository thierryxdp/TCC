def colchao (medidas, H,L):
    medidas.sort()
    
    altura=medidas[0]
    largura=merdidas[1]
    comprimento=medidas[2]
    
    if comprimento < H:
        return True
    
    if largura < H:
        return True
    
    if comprimento < H:
        return False