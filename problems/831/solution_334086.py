def lingua_p(palavra):
    i=0
    saida=palavra
    while i<=len(palavra):
        if palavra[i] in 'aAeEiIoOuU':
            return 'ok'
            
            
            
            '''saida.replace(palavra[i], palavra[i]+'p'+palavra[i])
    return saida'''