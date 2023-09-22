def uppCons(frase):
    """kgkdmfkg"""
    
    separa_frase = frase.upper().split()
    
    if "a" in separa_frase:
        o = find(separa_frase, "a")
        upper = separa_frase[o].upper
        return separa_frase