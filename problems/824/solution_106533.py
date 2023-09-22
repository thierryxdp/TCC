def uppCons(frase):
    """kgkdmfkg"""
    
    separa_frase = frase.split()
    
    if "B" in separa_frase:
        o = find(separa_frase, "B")
        frase = separa_frase[o].upper
        return separa_frase