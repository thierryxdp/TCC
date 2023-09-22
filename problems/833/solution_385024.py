def conta_numero(numero:int,matriz:list)->int:
    '''Função que retorna quantas vezes o número aparece na matriz'''
    cont=[]
    ind=0
    while ind<len(matriz):
        if numero in matriz:
        	cont.append(matriz[ind])
        ind=ind+1
    return len(cont)