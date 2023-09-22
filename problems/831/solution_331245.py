def lingua_p(frase):
    """
    Coloca um "p" após uma vogal, acrescido da mesma vogal
    str -> str
    """
    
    l = ["a", "e", "i", "o", "u", "à", "ã", "õ", "á", "é", "í", "ó", "ú", "â", "ê", "ô"]
    nfrase = frase.lower()
    x = len(nfrase)
    i = 0

    while i < x:
        for j in range(len(l)):
            if nfrase[i] == l[j]:
                nfrase = nfrase[0:(i+1)] + 'p' + nfrase[i:]
                i += 2
                x = len(nfrase)
                break
        i += 1
                
    
    return nfrase

    #lingua_p('exemplo') → epexepemplopo
    #lingua_p('então') → epentãpãopo
    #lingua_p('Caderno') → capadepernopo