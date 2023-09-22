def lingua_p(palavra):
    i=0
    saida=palavra
    while i<len(palavra):
        if palavra(i) in 'aAeEiIoOuU':
            saida.replace(palavra[i],'p')
        i=i+1
    return saida