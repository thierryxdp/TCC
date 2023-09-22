def conta_frases(texto):
    if '.' in texto:
        #str.find(texto,'.')
        ponto=str.split(texto,'.')
        #exclamacao=str.split(texto,"!")
        #interrogacao=str.split(texto,'?')
        #reticencias=str.split(texto,"...")
        #return len(ponto)
        if '!' in ponto:
            exclamacao=str.split(ponto,'!')
            #return len(exclamacao)
            if '?' in exclamacao:
                interrogacao=str.split(exclamacao,'?')
                #return len(interrogacao)
                if '...' in interrogacao:
                    reticencias=str.split(interrogacao,'...')
                    return len(reticencias)
    elif '!' in texto:
        exclamacao=str.split(texto,'!')
        return len(exclamacao)
    elif '?' in texto:
        interrogacao=str.split(texto,'?')
        return len(interrogacao)
    elif '' in texto:
        reticencias=str.split(texto,'...')
        return len(reticencias)