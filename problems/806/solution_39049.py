def colisao(ret1,ret2):
    
    if ret1[2]>ret2[4] or ret2[6]>ret1[0] or ret1[3]>ret2[2] or ret2[7]>ret1[1]:
        return True
    else:
        return False

# segunda etapa - calculo do resultado