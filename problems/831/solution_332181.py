def lingua_p(palavra):
    for x in palavra:
        if x in 'AEIOUaeiou':
            str.insert(palavra,str.index(palavra,x),'p'+x)
    return palavra