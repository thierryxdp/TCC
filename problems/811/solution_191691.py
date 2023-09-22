def colchao (lista,H,L):
    '''os paramentros da entradas são uma lista com um lista comtetendo as dimenssões do colchão em centímetro do menor para o maior e dois inteiros H (altura) e L (largura) da porta, em centímetros, a função deve retornar um dado boleano True se o calchão que tem forma de um paralelepípedo reto conseguir atravessar a porta, com uma de suas faces paralelas ao chão
    list->bool'''
    if int(H*L)>lista[0]*lista[1]:
        return True
    if int(H*L)>lista[0]*lista[2]:
        return True
    if int(H*L)>lista[1]*lista[2]:
        return True
    if int(H*L)<lista[0]*lista[1]:
        return False
    if int(H*L)<lista[0]*lista[2]:
        return False
    if int(H*L)<lista[1]*lista[2]:
        return False