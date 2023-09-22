def conta_numero(numero,matriz):
    '''retorna e conta vezes que número aparece na matriz
    int,list->int'''
    
    i=0
    
    for NumeroQualquer in matriz:
        i=i+list.count(NumeroQualquer,numero)
        
    return i