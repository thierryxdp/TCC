def bolos int(farinha,ovos,leite):
    if farinha < 2:
        return 'sem bolo'
    elif ovos < 3:
        return 'sem bolo'
    elif leite < 5:
        return 'sem bolo'
    else:
        return (farinha/2)+(ovos/3)+(leite/5)