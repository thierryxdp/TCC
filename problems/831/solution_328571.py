def lingua_p(palavra):
    resultado =''
    for i in len(palavra)-1:
        if palavra[i] in "aeiouáéíóú":
            resultado += palavra[i] +'p'+palavra[i]
        else:
            resultado += palavra[i]
    return resultado