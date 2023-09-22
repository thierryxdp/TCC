def vogal(palavra):
    if palavra in 'aeiouãêéúó':
        return True
    else:
        return False
def uppCons(frase):
    i = 0
    r = ''
    while i <len(frase):
        if vogal(frase[i]) == False:
            r = r + str.upper(frase[i])
        else:
                if vogal(frase[i]) == True:
                    r = r + (frase[i])
        i = i + 1
    return r