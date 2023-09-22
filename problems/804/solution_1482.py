def filtra_pares(num):
    ''' Dando como entrada 4 números inteiros numa tupla, a funcao retorna
    outra tupla, que mostra quais sao os numeros pares dentre os dados, 
    colocados na mesma ordem;
    
    tuple -> tuple  '''
    
    num[0],num[1],num[2],num[3] 
    
    par1 = (num[0])%2 == 0
    par2 = (num[1])%2 == 0
    par3 = (num[2])%2 == 0
    par4 = (num[3])%2 == 0
    
    
    if (par1):
        if (par2):
            if (par3):
                if (par4):
                    return num[0],num[1],num[2],num[3]
                    
                elif (not(par4)):
                    return num[0],num[1],num[2]
                
            elif (not(par3)):
                if (par4):
                    return num[0],num[1],num[3]
                    
                elif (not(par4)):
                    return num[0],num[1]
    
        elif (not(par2)):
            if (par3):
                if (par4):
                    return num[0],num[2],num[3]
                    
                elif (not(par4)):
                    return num[0],num[2]
                
            elif (not(par3)):
                if (par4):
                    return num[0],num[3]
                    
                elif (not(par4)):
                    return num[0],
                
    elif (not(par1)):
        if (par2):
            if (par3):
                if (par4):
                    return num[1],num[2],num[3]
                    
                elif (not(par4)):
                    return num[1],num[2]
                
            elif (not(par3)):
                if (par4):
                    return num[1],num[2]
                    
                elif (not(par4)):
                    return num[1],
                
        elif (not(par2)):
            if (par3):
                if (par4):
                    return num[2],num[3]
                    
                elif (not(par4)):
                    return num[2],
                
            elif (not(par3)):
                if (par4):
                    return num[3],
                    
                elif (not(par4)):
                    return tuple()