def colchao(medidas,H,L):
    '''função em que dada uma lista (medidas) com as dimensões de um colchão
    em centímetros, ordenadas da menor para a maior, e dois números inteiros
    (H e L), corespondentes respectivamente à altura e à largura da porta em
    centímetros retorne 'True' se o colchão passar pela porta e 'False' se não;
    list, int, int -> bool'''
    porta=medidas[0]
    alt=medidas[2]
    lg=medidas[1]
    if porta<=H and lg<=L:
        return True
    elif porta<=H and alt<=L:
        return True
    elif lg<=H and alt<=L:
        return True
    elif alt<=H and lg<=L:
        return True
    elif porta<=L and alt<=H:
        return True
    elif porta<=L and lg<=H:
        return True