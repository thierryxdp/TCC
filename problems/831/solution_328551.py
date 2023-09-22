def lingua_p(string):
    ''''''
    acumulador = ''
    for i in range(len(string)):
        if string[i] in 'AEIOUaeiouáéíóú':
            acumulador = acumulador + str(string[i])+'p'+str(string[i])
        else:
            acumulador = acumulador + string[i]
    return acumulador