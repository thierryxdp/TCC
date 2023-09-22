def lingua_p(palavra):
    '''.....'''
    for i in len(palavra):
        if palavra[i] in 'aeiouAEIOU':
            palavra = str.replace(palavra, palavra[i], str(palavra[i])+'p'+str(palavra[i])
    return palavra