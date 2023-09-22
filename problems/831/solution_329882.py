def lingua_p(palavra):
    '''Recebe uma palavra e retorna a mesma palavra na lingua do P.
str->str'''
    papalapavrapa=''
    for x in palavra:
        if x not in 'AÂÁEÊÉIÍOÓÔÚUaáâeéêiíoóôuú':
            papalapavrapa+= str(x)
        if x in 'AÂÁEÊÉIÍOÓÔÚUaáâeéêiíoóôuú':
            papalapavrapa+= str(x) + 'p' + str(x)
    return papalapavrapa