def uppCons(frase):
    """kgkdmfkg"""
    
    consoantes = ['B','C','D','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z']
    if str(consoantes).upper in str(frase):
        index = frase.index(consoantes.upper())
        frase = frase.split()
        frase[index] = consoantes.upper()
        frase = " ".join(frase)
        return frase