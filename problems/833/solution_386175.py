def conta_numero(numero,matriz):
    ''''''
    inteiro=[numero]
    
    for linha in matriz:
        nv_linha=linha[:]
        inteiro=inteiro+[nv_linha]
        
    
    return inteiro