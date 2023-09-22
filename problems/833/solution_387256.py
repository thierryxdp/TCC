def conta_numero(numero,matriz):
    
    ocorrencias=0
    
    for linha in matriz:
        for posicao in linha:
            if posicao==numero:
                ocorrencias+=1
            
    return ocorrencias