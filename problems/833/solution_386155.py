def conta_numero(numero,matriz):
    ''''''
    numero=[]
    
    for linha in matriz:
        nv_linha=linha[:]
        numero=list.count(matriz,numero)+[nv_linha]
        
    return numero