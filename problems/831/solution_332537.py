def lingua_p(palavra):
    for i in palavra:
        if i in 'AEIOUaeiou':
            lp=palavra[0:(str.index(palavra,i)+1)]+'p'+i+palavra[((str.index(palavra,i)+4),0]
    return lp