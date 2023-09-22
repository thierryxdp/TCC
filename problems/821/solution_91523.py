def fatorial(numero):
    '''dado um numero, retorna o fatorial deste mesmo numero
    :param numero:int->int
    :return: int->int
    '''
    contador= 1
    fat= 1
    while contador <= numero:
        fat*= contador
        contador+=1
    
    return fat