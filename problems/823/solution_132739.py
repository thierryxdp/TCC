def faltante(inteiros):
    inteiros.sort()
    
    atual = 1
    for i in inteiros:
        if i != atual:
            break
            
        atual += 1
        
    return atual