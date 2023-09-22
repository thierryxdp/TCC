def posLetra (string, letra, num):
    i = 0
    while i < len(string):
        if string.count(letra)>= num:
            i = i+1
            return string.count(letra)
        else:
            return -1