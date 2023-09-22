def soma_h (num):
    cont = 0.0
    for i in range (1, num+1):
        cont+= 1/i
        return round(cont, 2)