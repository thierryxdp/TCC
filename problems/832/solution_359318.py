def eh_quadrada(lista):
    x=0
    y=0
    for a in lista:
        x+=1
        for b in a:
            y+=1
            if y == x:
                return True
            else:
                return False