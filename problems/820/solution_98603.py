def posLetra(string,letra,num):
    '''str, str, inr -> str'''
    cont = 0
    for i in string:
        if i == letra:
            cont+= 1
        elif num == cont:
            return string.index(i)
    return -1