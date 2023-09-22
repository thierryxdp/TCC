def inverte(f: str) 
    f == ()
    """ fsp = Frase Sem Pontuação"""
    
    fsp = str.replace(f, ":", " ")
    fsp1 = str.replace(fsp, ",", " ")
    fsp2 = str.replace(fsp1, ".", " ")
    fsp3 = str.replace(fsp2, ";", " ")
    fsp4 = str.replace(fsp3, "!", " ")
    fsp5 = str.replace(fsp4, "-", " ")
    fsp6 = str.replace(fsp5, "?", " ")
    
    fpfinal = str.split(fsp6, -1)
    return fpfinal