def lingua_p(palavra):
    a = list(palavra)
    r = ''
    for i in a:
        if i in 'AEIOUaeiouÁÉÍÓÚáéíóúÂÊÎÔÛâêîôû':
            r += i + 'p' + i
        else:
            r += i
    return r