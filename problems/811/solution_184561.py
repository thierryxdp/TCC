def porta(medidas, H, L):
    if (H > L):
        if(medidas[1] <= H and medidas[0] <= L):
            return True
        else:
            return False
    else:
        if(medidas[0] <= H and medidas[1] <= L):
            return True
        else:
            return False