def colchao (lista,H,L):
    '''os paramentros da entradas são uma lista com um lista comtetendo as dimenssões do colchão em centímetro do menor para o maior e dois inteiros H (altura) e L (largura) da porta, em centímetros, a função deve retornar um dado boleano True se o calchão que tem forma de um paralelepípedo reto conseguir atravessar a porta, com uma de suas faces paralelas ao chão
    list->bool'''
    if H>=lista[1] and L>=lista[2]:
        return True
    if H>=lista[1] or L>=lista[2]:
        return True
    else:
        return False