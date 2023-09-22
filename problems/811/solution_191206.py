def colchao(medidas, H, L):

    a = medidas.sort()

    if H >= medidas[2]:

        if L >= medidas[1] or L >= medidas[0]:

            return True
        
        else:

            return False
    
    elif L >= medidas[2]:

        if H >= medidas[0] or medidas[1]:

            return True

        else:
            
            return False
    
    else:

        return a