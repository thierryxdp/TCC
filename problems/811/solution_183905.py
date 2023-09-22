def colchao(medidas, H, L):
  
   A,B,C=medidas[0],medidas[1],medidas[2]
     if medidas[1]<=L and medidas[2]<=H:
        return True
    if medidas[0]<=L and medidas[1]<=H:
        return True
    if medidas[0]<=L and medidas[2]<=H:
        return True
    else:
        return False