def colchao(medidas, H, L):
    maior_lado = max(medidas)
    medidas.remove(maior_lado)
    maior_que_H = 0
    maior_que_L = 0
    
    for x in medidas:
        if(x > H):
            maior_que_H += 1
        elif(x > L):
            maior_que_L += 1
    
    if(maior_que_H > 1 or maior_que_L > 1):
        return False
    else:
        return True