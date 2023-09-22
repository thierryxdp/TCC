def conta_numero(numero,matriz):
    ''''''
    inteiro=[]
    
    for linha in matriz:
        nv_linha=linha[:]
        inteiro=inteiro+[nv_linha]
        if inteiro in matriz:
            return inteiro