def bolos (farinha,ovos,leite):
    """Função que determinará quantidade de bolos, Input int, int, int. Return int"""
    
    a = 2
    b = 3
    c = 5
    
    if farinha%a == 0 and ovos%b == 0 and leite%c == 0:
        return farinha//a
    
    elif farinha == 0 or ovos == 0 or leite == 0:
        return 0
    
    elif farinha%a > ovos%b or farinha%a > leite%c:
        return farinha//a
    
    elif ovos%b > farinha%a or ovos%b > leite%c:
        return ovos//b
    
    elif leite%c > farinha%a or leite%c > ovos%b:
        return leite//c