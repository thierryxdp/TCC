def lingua_p(palavra):
    a=''
    for i in range(len(palavra)):
        if palavra[i] in 'ÁÉAEIOUáéaeiou':
            a+=palavra[i].replace(palavra[i],palavra[i]+'p'+palavra[i])
        else:
            a+= palavra[i]
    return a