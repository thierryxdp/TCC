def conta_numero(numero,matriz):
    ''' Função que retornar quantas vezes o numero foi repitido 
        matriz.
        int,list(list)--->>int'''
    x=0
    for i in matriz:
        if i == numero:
            x+=1
        
    return x