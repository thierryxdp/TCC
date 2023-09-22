def conta_numero(numero,matriz):
    '''funçao que retorna o número de vezes que um nunero esta presente ma matriz''' 
    '''int,list[list]->int'''
    vezes=0 
    for i in range(len(matriz)):
        for j in (matriz[i]):
            if j==numero:
                vezes=vezes+1 
    return vezes