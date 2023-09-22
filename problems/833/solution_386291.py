def conta_numero(numero,matriz):
    '''Fazer uma funcao que retorne quantas vezes o numero aparece na matriz;
    int, list -> int'''
    
    quantidade = 0
    
    for i in matriz:
        for j in i:
            if numero == j:
                quantidade = quantidade + 1
                
    return quantidade