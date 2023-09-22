def conta_numero(numero,matriz):
    ''''''
    nv_matriz=[]
    
    for linha in matriz:
        nv_linha=linha[:]
        nv_matriz=nv_matriz+[nv_linha]
        
        if numero in matriz[0]:
            return list.count(matriz,numero)