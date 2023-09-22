'''Resolução com While '''
def soma_h(n):
    h = 0
    contador = 0
    limite = n+1
    
    while contador <= limite:
        h += 1/ contador
        contador += 1
    h = round(h,2)
    return h