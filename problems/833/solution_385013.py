from collections import Counter
def conta_numero(numero,matriz):
    '''...'''
    
    R=[]
    n_linha=len(matriz)
    n_coluna=len(matriz[0])
    
    for i in range(n_linha):
        linha = n_coluna*[0]
        list.append(R,linha) 
        
    for i in range(n_linha):
        for j in range(n_coluna):
            if numero in matriz:
                cont = list.count(matriz,numero) 
                cont+=1
    return cont