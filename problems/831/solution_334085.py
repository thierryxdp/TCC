def lingua_p(palavra):
    i=0
    saida=palavra
    while i<=len(palavra):
        if palavra[i] in 'aAeEiIoOuU':
            saida.replace(palavra[i], palavra[i]+'p'+palavra[i])
    return saida