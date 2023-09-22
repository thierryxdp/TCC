def lingua_p(palavra):
    '''Recebe uma palavra e retorna a mesma palavra na lingua do P.
str->str'''
    papalapavrapa=''
    for letra in palavra:
        if letra not in 'AÂÁEÊÉIÍOÓÔÚUaáâeéêiíoóôuú':
            papalapavrapa+= str(letra)
        if letra in 'AÂÁEÊÉIÍOÓÔÚUaáâeéêiíoóôuú':
            papalapavrapa+= str(letra) + 'p' + str(letra)
    return papalapavrapa