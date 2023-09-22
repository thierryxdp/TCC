def colchao(medidas,H,L):
    '''função em que dada uma lista (medidas) com as dimensões de um colchão
    em centímetros, ordenadas da menor para a maior, e dois números inteiros
    (H e L), corespondentes respectivamente à altura e à largura da porta em
    centímetros retorne 'True' se o colchão passar pela porta e 'False' se não;
    list, int, int -> bool'''
    porta=medidas[0]
    Alt=medidas[2]
    lg=medidas[1]
    if Porta<=H and lg<=L:
        return True
    else:
    if Porta<=H and Alt<=L:
        return True
    else:
    if lg<=H and Alt<=L:
        return True
    else:
    if Alt<=H and lg<=L:
        return True
    else:
    if Porta<=L and Alt<=H:
        return True
    else:
    if Porta<=L and lg<=H:
        return True