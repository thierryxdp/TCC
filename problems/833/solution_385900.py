def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes que um numero aparece na matriz'''
    '''int, list -> int'''
    
    i=0
    l=[]
    for numero in matriz:
        t=len(matriz[i])
        if i < t:
            quant=list.count(matriz, numero)
            list.append(l, quant)
            cont_num=sum(l)
            i=i+1
        
    return cont_num