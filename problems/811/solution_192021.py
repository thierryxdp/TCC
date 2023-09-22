def colchao (medidas,H,L):
    
    altura = int(medidas[0]) 
    largura = int(medidas[1]) 
    if int(H)>= int(L):
        maior_lado = H
        menor_lado = L
    else:
        maior_lado = L
        menor_lado = H
        
    if altura<=menor_lado and largura<=maior_lado:
        return True
    else:
        return False