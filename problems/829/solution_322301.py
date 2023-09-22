def soma_h(numero):
    '''Dado um numero, a função calcula H com o numero de termos
    ela retorna seu resultado com 2 casas decimais.
    int->float'''
    
    H=1
    indice=2
    
    while indice<=numero:
        H=H+1/indice
        indice=indice+1
    return round(H,2)