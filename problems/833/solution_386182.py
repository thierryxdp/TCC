def conta_numero(numero,matriz):
    ''''''
    inteiro=[]
    
    for linha in matriz:
        nv_linha=linha[:]
        inteiro=inteiro+[nv_linha]
        
    inteiro=list.count(matriz[0:1],numero)
    return inteiro