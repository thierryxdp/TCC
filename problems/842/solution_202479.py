def pontos_por_time(LP):
    Ji=LP[0]
    Jv=LP[1]
    
    PJI = Ji[2]
    PJV = Jv[2]
    
    if PJI[0]>PJI[1]:
        PFI=3
        PCI=0
    elif PJI[0]>PJI[1]:
        PCI=3
        PFI=0
    else:
        PCI=1
        PFI=1
    
    if PJV[0]>PJV[1]:
        PFI=3
        PCI=0
    elif PJV[0]>PJV[1]:
        PCF=3
        PFF=0
    else:
        PCF=1
        PFF=1
        
    PC=PCI=PCF
    PF=PFF=PFI
    
    resultado={Ji[0]:PF, Ji[1]:PC}
    return resultado