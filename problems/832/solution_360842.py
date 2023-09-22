def eh_quadrada(lista):
    for i in lista:
        if len(i)==len(lista):
            return True
        elif len(lista)==0:
            return True
        else:
            return False