def colchao(medidas, H, L):

    a = 0
    if H > L:

        a = H

        b = L
    
        if medidas[0] <= a:

            if medidas[1] <= b or medidas[2] <= b:

                return True
            
            else:

                return False
        elif medidas[1] < a:

            if medidas[0] <= b or medidas[2] <= b:

                return True
            
            else:

                return False

        elif medidas[2] <= a:

            if medidas[0] <= b or medidas[1] <= b:

                return True
            
            else:

                return False
    
    else:

        a = L

        b = H 

        if medidas[0] <= a:

            if medidas[1] <= b or medidas[2] <= b:

                return True
            
            else:

                return False
        elif medidas[1] < a:

            if medidas[0] <= b or medidas[2] <= b:

                return True
            
            else:

                return False

        elif medidas[2] <= a:

            if medidas[0] <= b or medidas[1] <= b:

                return True
            
            else:

                return False