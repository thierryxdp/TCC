def conta_numero(numero,matriz):
    '''conta e retorna quantas vezes um numero inteiro
    informado aparece na mattriz fornecida
    int,list(list) -> int'''
    quant = 0    
    for i in matriz:
        for j in i:
            if numero == j:
                quant += 1        
    return quant