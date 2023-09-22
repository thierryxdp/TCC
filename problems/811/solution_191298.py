def colchao(medidas,H,L):
    
   if medidas[0]> L:
        return False
   if (medidas[1]**2 - medidas[0]**2)**0.5 > H:
        return False
   else:
        return True