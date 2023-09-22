def eh_quadrada(l):
    if l == []:
        return True
    else:
        if len(l) == len(l[0]):
            return True
        else:
            return False