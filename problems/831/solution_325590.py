def lingua_p(string):

    minuscula=str.lower(string)
    palavra=''
    contador=0
    

    for x in minuscula:
        if x in 'aeiouáéíóúâã':
            palavra=palavra+minuscula[contador]+'p'+minuscula[contador]
        else:
            palavra=palavra+minuscula[contador]

        contador=contador+1

    return palavra