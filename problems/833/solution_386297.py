def conta_numero(numero,matriz):
    '''Fazer uma funcao que retorne quantas vezes o numero aparece na matriz;
    int, list -> int'''
    
    quantidade = 0
    
    for linha in matriz:
        for coluna in linha:
            if numero == coluna:
                quantidade = quantidade + 1
                
    return quantidade