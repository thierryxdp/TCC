def colchao(medidas, H, L):
    maior_lado = max(medidas)
    medidas.remove(maior_lado)
    maior_que_lado = 0
    
    for x in medidas:
        if(x > H):
            maior_que_lado += 1
        if(x > L):
            maior_que_lado += 1
        if(maior_que_lado == 2):
            return False
        else: 
            maior_que_lado = 0
    
    return True