def colchao(lista,h,l):
    if lista[0]<=h and lista[1]<=l:
        return True
    if lista[0]<=l and lista[1]<=h:
        return True
    else:
        return False