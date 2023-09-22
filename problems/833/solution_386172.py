def conta_numero(numero,matriz):
    ''''''
    inteiro=[]
    
    for linha in matriz:
        nv_linha=linha[:]
        inteiro=inteiro+[nv_linha]
        
    a = list.count(matriz[0],numero)
    return inteiro