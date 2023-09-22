def posLetra(palavra,letra,num):
    ''''''
    nl = 0
    i= 0
    while i < len(palavra):
        str.find(palavra,letra,nl)
        if nl != num:
        nl = nl + 1
        i = i + 1
    return str.find(palavra,letra,nl-1)