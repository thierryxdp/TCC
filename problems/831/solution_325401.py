def lingua_p(palavra):
    for i in 'aeiou':
        palavra = str.replace(palavra, i, i+'p'+i)
    return palavra