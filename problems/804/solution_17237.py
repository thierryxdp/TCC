def filtra_pares(tupla):
    '''função que dados 4 elementos de uma tupla, retorna uma nova tupla mantendo somente os pares; tuple-> tuple '''
    elemento1=int(tupla[0])
    elemento2=int(tupla[1])
    elemento3=int(tupla[2])
    elemento4=int(tupla[3])  
    if elemento1%2==0 and elemento2%2!=0 and elemento3%2!=0 and elemento4%2!=0:
        return (elemento1,)   
    elif elemento1%2!=0 and elemento2%2==0 and elemento3%2!=0 and elemento4%2!=0:
        return (elemento2,)   
    elif elemento1%2!=0 and elemento2%2!=0 and elemento3%2==0 and elemento4%2!=0:
        return (elemento3,)   
    elif elemento1%2!=0 and elemento2%2!=0 and elemento3%2!=0 and elemento4%2==0:
        return (elemento4,)   
    elif elemento1%2==0 and elemento2%2==0 and elemento3%2!=0 and elemento4%2!=0:
        return (elemento1,)+(elemento2,)    
    elif elemento1%2==0 and elemento2%2==0 and elemento3%2==0 and elemento4%2!=0:
        return (elemento1,)+(elemento2,)+(elemento3,)   
    elif elemento1%2==0 and elemento2%2!=0 and elemento3%2==0 and elemento4%2!=0:
        return (elemento1,)+(elemento3,)   
    elif elemento1%2!=0 and elemento2%2==0 and elemento3%2==0 and elemento4%2!=0:
        return (elemento2,)+(elemento3,)      
    elif elemento1%2==0 and elemento2%2==0 and elemento3%2==0 and elemento4%2==0:
        return (elemento1,)+(elemento2,)+(elemento3,)+(elemento4,)
    elif elemento1%2==0 and elemento2%2!=0 and elemento3%2==0 and elemento4%2!=0:
        return (elemento1,)+(elemento3,)
    elif elemento1%2==0 and elemento2%2==0 and elemento3%2!=0 and elemento4%2==0:
        return (elemento1,)+(elemento2,)+(elemento4,)
    elif elemento1%2==0 and elemento2%2!=0 and elemento3%2==0 and elemento4%2==0:
        return (elemento1,)+(elemento3,)+(elemento4,)
    elif elemento1%2!=0 and elemento2%2==0 and elemento3%2==0 and elemento4%2==0:
        return (elemento2,)+(elemento3,)+(elemento4,)
    elif elemento1%2!=0 and elemento2%2==0 and elemento3%2!=0 and elemento4%2==0:
        return (elemento2,)+(elemento4,)
    elif elemento1%2!=0 and elemento2%2!=0 and elemento3%2==0 and elemento4%2==0:
        return (elemento3,)+(elemento4,)    
    else:
        return ()