def eh_quadrada(lista):
    c=0
    for i in range(len(lista)):
        for j in range(len(lista[c])):
            if i==j:
                c=+1
                return True
            else:
                return False