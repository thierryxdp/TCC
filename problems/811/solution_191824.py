def colchao(medidas,h,l):
    
     if medidas[1] < h:
        return True
     if medidas[2] < l: 
        return True
     if medidas[1] < l:
        return True
     if medidas[2] > h:
        return True
     else:
        return False