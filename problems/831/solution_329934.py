def lingua_p(palavra):
    for i in palavra:
        if i in 'aeiouAEIOU':
            i='p'+i+'p'
    return palavra