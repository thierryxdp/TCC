def carros(np,cap=5):
    """Funcao que calcule o numero exato de carros necessariospara esta viagem, considerando que seja dado como entrada o numero de pessoas,np, caso o grupo de carros nao for  de tamnho convecional deverá ser exposto  na entrada"""
    5<=cap
    if np<=5:
        return 1
    elif np==cap:
        return 1
    else:
        return np//cap