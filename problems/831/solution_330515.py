def lingua_p(palavra):
    '''dada uma palavra na lingua portuguesa na forma de str
    a funçao nos devolve a palavra na lingua do p tambem
    em str
    str-->str'''
    somaStr=''
    for i in range(len(palavra)):
        if palavra[i] in 'aAáÁàÀãÃeEéÉiIíÍoOóÓôÔuUúÚ':
            somaStr=somaStr+palavra[i]+'p'+palavra[i]
        if palavra[i] not in 'aAáÁàÀãÃeEéÉiIíÍoOóÓôÔuUúÚ':
            somaStr=somaStr+palavra[i]
    return somaStr