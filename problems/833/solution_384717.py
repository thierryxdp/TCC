from collections import Counter
def conta_numero(numero,matriz):
    
    n_linha = len(matriz)
    n_coluna = len(matriz[0])
    R=[]
    pos=0
    for i in range(n_coluna):
        linha = n_coluna*[0]
        list.append(R,linha)
    qtd=0
    for e in matriz:
        if numero[e] == numero:
            qtd+=1
            qtd=R*count(numero)
    return qtd