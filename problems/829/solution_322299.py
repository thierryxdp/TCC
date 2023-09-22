def soma_h(numero):
    '''...'''
    
    H=1
    indice=2
    
    while indice<=numero:
        H=H+1/indice
        indice=indice+1
    return round(H,2)