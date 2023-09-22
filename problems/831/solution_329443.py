def lingua_p(palavra):
    papalapavrapa=''
    for letra in palavra:
        if letra not in 'AEIOUaeiou':
            papalapavrapa+= str(letra)
        if letra in 'AEIOUaeiou':
            papalapavrapa+= str(letra) + 'p' + str(letra)
    return papalapavrapa