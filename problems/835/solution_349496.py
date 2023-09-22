def melhor_volta(corrida):
    '''Calcula e retorna a melhor volta, o corredor que a fez
       e a volta em que foi realizada este tempo'''
    
    melhores_voltas = []
    numero_volta = []
    
    for corredor in corrida:
        
        menor_tempo = min(corredor)
        
        numvolta = corredor.index(menor_tempo) + 1
        
        melhores_voltas.append(menor_tempo)
        
        numero_volta.append(numvolta)
        
    melhor_tempo = min(melhores_voltas)
    
    primeiro = melhores_voltas.index(melhor_tempo) + 1
    
    numero = numero_volta[primeiro - 1]
    
    return (primeiro,melhor_tempo,numero)