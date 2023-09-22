def conta_numero(numero, matriz):
    '''
    Funcao percorre a martiz inteira e ver se tem numero int
    '''
  
    total= 0
    
    for item in matriz:
       
        for item2 in matriz:
            if item2 == numero:
                conta += 1
                
    return total