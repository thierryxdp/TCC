def conta_numero(numero,matriz):
    ''''''
    inteiro=[]
    matriz=0
    
    for linha in matriz:
        nv_linha=linha[:]
        inteiro=inteiro+[nv_linha]
        
    inteiro=list.count(matriz,numero)
    return inteiro