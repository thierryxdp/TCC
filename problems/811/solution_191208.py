def colchao(medidas, H, L):

    a = medidas.sort()

    if H >= medidas[2]:
    

        if L >= medidas[1] or L >= medidas[0]:

            return True
        
        else:

            return False

    elif H >= medidas[1]:

        if L>= medidas[0]:

            return True

        else:
            
            return False
    
    elif L >= medidas[2]:

        if H >= medidas[0] or H >= medidas[1]:

            return True

        else:
            
            return False

    elif L >= medidas[1]:

        if H >= medidas[0]:

            return True
    
    else:

        return False