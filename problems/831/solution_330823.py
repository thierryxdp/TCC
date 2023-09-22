def lingua_p(palavra):
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    i=0
    for i in range(len(palavra)):
        if palavra[i] in vogal:
            i=i+palavra[i]+'p'+palavra[i:]
        if palavra[i] not in vogal:
            palavra[i]
            i=i+palavra[i]
    return i