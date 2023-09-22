from collections import Counter
def conta_numero(numero,matriz):
    
    n_linha = len(matriz)
    n_coluna = len(matriz[0])
    R=[]
    
    for i in range(n_coluna):
        linha = n_coluna*[0]
        list.append(R,linha)
    
    for e in matriz:
        if e == numero:
            list.append(R,e)
            list.count(R,e)
    return e