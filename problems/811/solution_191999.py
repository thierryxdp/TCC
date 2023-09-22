def colchao(medidas,H,L):
 '''função em que dada uma lista (medidas) com as dimensões de um colchão
    em centímetros, ordenadas da menor para a maior, e dois números inteiros
    (H e L), correspondentes respectivamente à altura e à largura da porta em
    centímetros retorne 'True' se o colchão passar pela porta e 'False' se não;
    list, int, int -> bool'''
    lg=medidas[1]
    Alt=medidas[2]
    Port=medidas[0]
    if Port<=H and lg<=L:
        return True
    elif Port<=H and Alt<=L:
        return True
    elif lg<=H and Alt<=L:
        return True
    elif Alt<=H and lg<=L:
        return True
    elif Port<=L and Alt<=H:
        return True
    elif Port<=L and lg<=H:
        return True