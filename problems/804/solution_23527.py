def filtra_pares(x):
    """função que recebe uma tupla com quatro elementos inteiros
    como parâmentro e retorna uma nova tupla contendo apenas os
    elementos pares da tupla original na mesma ordem em que estavam"""
    par1=x[0]%2==0
    par2=x[1]%2==0
    par3=x[2]%2==0
    par4=x[3]%2==0
    if (par1 and par2 and par3 and par4):
        return tuple(x)
    
    elif (par1 and par2 and par3):
        return (x[0],x[1],x[2])

    elif (par2 and par3 and par4):
        return(x[1],x[2],x[3])

    elif (par1 and par2 and par4):
        return (x[0],x[1],x[3])
    
    elif(par1 and par3 and par4):
        return (x[0],x[2],x[3])
    
    elif (par1 and par2):
        return(x[0],x[1])
    
    elif (par3 and par4):
        return (x[2],x[3])
          
    elif(par1 and par3):
        return (x[0],x[2])
    
    elif(par1 and par4):
        return (x[0],x[3])
    
    elif(par2 and par3):
        return (x[1],x[2])
    
    elif(par2 and par4):
        return (x[1],x[3])
    
    elif (par1):
        return "("+str (x[0])+","+")"
    
    elif (par2):
        return "("+str (x[1])+","+")"
    
    elif (par3):
        return "("+str (x[2])+","+")"

    elif (par4):
        return "("+str (x[3])+","+")"

    else:
        return ()
#Start your python function here