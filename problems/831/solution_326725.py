def lingua_p(palavra):
    i=0
    p =''
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiouÁÉÍÓÚáéíóú':
            p= p+palavra[i]+'p'+palavra[i]
        else:
                p=p+palavra[i]
        i+1
    return p