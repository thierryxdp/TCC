#def bolos(farinha,ovos,leite):
    '''dados os ingredientes (a,b,c) retorna um numeor inteiro de bolos'''
    a=farinha//2
    b=ovos//3
    c=leite//5
 #   return min(a,b,c)

def bolos(far, ovos, leite):
    if (far//2)*2 <= ovos//3 + leite//5:
        return far//2
    elif (ovos//3)*2 <= far//2 + leite//5:
        return ovos//3
    elif (leite//5)*2 <= far/2 + ovos//3:
        return leite//5