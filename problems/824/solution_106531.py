def uppCons(frase):
    """kgkdmfkg"""
    
    separa_frase = frase.upper().split()
    
    if "B" in separa_frase:
        o = find(separa_frase, "b")
        frase = separa_frase[o].upper
        return separa_frase