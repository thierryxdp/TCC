def filtra_pares(s):
    filtrado=[]
    if (s[0])/2==int((s[0])/2):
        filtrado.append(s[0])
        
    if s[1]/2==int(s[1]/2):
        filtrado.append(s[1])
        
    if s[2]/2==int(s[2]/2):
        filtrado.append(s[2])

    if s[3]/2==int(s[3]/2):
        filtrado.append(s[3])

    filtrado1=tuple(filtrado)
    return(filtrado1)