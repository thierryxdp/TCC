def colchao(lista):
    if lista[0]<=lista[3] and lista[1]<=lista[4]:
        return True
    if lista[0]<=lista[4] and lista[1]<=lista[3]:
        return True
    else:
        return False