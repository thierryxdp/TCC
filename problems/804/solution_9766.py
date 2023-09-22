def filtra_pares(tupla):
    
    resto = (tupla[0]%2,tupla[1]%2,tupla[2]%2,tupla[3]%2)
    if resto[0]!=0 and resto[1]!=0 and resto[2]!=0:
        return (tupla[3],)
    elif resto[0]!=0 and resto[1]!=0:
        return (tupla[2],tupla[3])
    elif resto[0]!=0:
        return (tupla[1],tupla[2],tupla[3])
    elif resto[1]!=0 and resto[2]!=0 and resto[3]!=0:
        return (tupla[0],)
    elif resto[0]!=0 and resto[2]!=0 and resto[3]!=0:
        return (tupla[1],)
    else: 
        return tupla