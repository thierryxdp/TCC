def lingua_p(palavra):
    palavra=str.lower(palavra)
    palavra_p= ''
    for i in ranged(len(palavra):
        if palavra[i] in 'aeiouáéíóúã':
            palavra_p+= palavra[i]+'p'+palavra[i]
        else:
            palavra_p+= palavra[i]
    return palavra_p