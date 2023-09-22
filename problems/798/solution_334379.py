def freq_palavras(frases):
    '''...'''
    str.strip(frases)
    
    um=frases[0]
    dois=frases[1]
    tres=frases[2]
    
    umx=len(str.split(frases))
    doisx=str.count(frases,dois)
    tresx=str.count(frases,tres)
   
    dic={um:umx}
    
    return dic