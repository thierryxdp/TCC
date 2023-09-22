def bolos (farinha=2,ovos=3,leite=5):
    if farinha < 2:
        return int(0)
    elif ovos < 3:
        return int(0)
    elif leite < 5:
        return int(0)
   	elif farinha/2<=ovos/3 and leite/5:
        return farinha/2
    elif ovos/3<=farinha/2 and leite/5:
        return ovos/3
    elif leite/5<=farinha/2 and ovos/3:
        return leite/5