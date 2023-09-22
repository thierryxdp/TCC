def faltante(lista):
    i=1
    while i<99:
        if i not in lista:
            return i
        i+=1