def bolos (farinha,ovos,leite):
    """Função que determinará quantidade de bolos, Input int, int, int. Return int"""
    
    a = 2
    b = 3
    c = 5
    
    if farinha%a == 0 and ovos%b == 0 and leite%c = 0:
        return farinha//a
    elif farinha%a != 0 or ovos%b != 0 or leite%c != 0:
        return (farinha//a)-1