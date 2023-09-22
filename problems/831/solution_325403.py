def lingua_p(palavra):
    for i in 'aeiouéáú':
        palavra = str.replace(palavra, i, i+'p'+i)
    return palavra