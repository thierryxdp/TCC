def bolos int(farinha,ovos,leite):
    bolo=2*farinha+3*ovos+5*leite
    if farinha < 2:
        return 'sem bolo'
    elif ovos < 3:
        return 'sem bolo'
    elif leite < 5:
        return 'sem bolo'
    else:
        return bolo