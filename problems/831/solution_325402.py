def lingua_p(palavra):
    for i in 'aeioué':
        palavra = str.replace(palavra, i, i+'p'+i)
    return palavra