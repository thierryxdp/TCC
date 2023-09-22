def conta_numero(numero,matriz):
    ''''''
    inteiro=[]
    
    for linha in matriz:
        nv_linha=linha[:]
        inteiro=list.count(matriz,inteiro)+[nv_linha]
        
    return inteiro