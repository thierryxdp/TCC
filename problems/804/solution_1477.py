def filtra_pares(numero1,numero2,numero3,numero4):
    ''' Dando como entrada 4 números inteiros numa tupla, a funcao retorna
    outra tupla, que mostra quais sao os numeros pares dentre os dados, 
    colocados na mesma ordem;
    
    tuple -> tuple  '''
    
    
    par1 = (numero1)%2 == 0
    par2 = (numero2)%2 == 0
    par3 = (numero3)%2 == 0
    par4 = (numero4)%2 == 0
    
    
    if (par1):
        if (par2):
            if (par3):
                if (par4):
                    return numero1,numero2,numero3,numero4
                    
                elif (not(par4)):
                    return numero1,numero2,numero3
                
            elif (not(par3)):
                if (par4):
                    return numero1,numero2,numero4
                    
                elif (not(par4)):
                    return numero1,numero2
    
        elif (not(par2)):
            if (par3):
                if (par4):
                    return numero1,numero3,numero4
                    
                elif (not(par4)):
                    return numero1,numero3
                
            elif (not(par3)):
                if (par4):
                    return numero1,numero4
                    
                elif (not(par4)):
                    return numero1
                
    elif (not(par1)):
        if (par2):
            if (par3):
                if (par4):
                    return numero2,numero3,numero4
                    
                elif (not(par4)):
                    return numero2,numero3
                
            elif (not(par3)):
                if (par4):
                    return numero2,numero4
                    
                elif (not(par4)):
                    return numero2
                
        elif (not(par2)):
            if (par3):
                if (par4):
                    return numero3,numero4
                    
                elif (not(par4)):
                    return numero3
                
            elif (not(par3)):
                if (par4):
                    return numero4
                    
                elif (not(par4)):
                    return tuple()