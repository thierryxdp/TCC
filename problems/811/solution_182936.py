def medidas(a,b,c):
    return (a,b,c)

def colchao (medidas, H, L):
    if medidas[1]>H and L>medidas[2]:
        return True
    
    if medidas[1]>H and medidas[2]>L:
        return False
   
    if H>medidas[1] and L>medidas[2]:
        return True
    
    if H>medidas[1] and medidas[2]>L:
        return True