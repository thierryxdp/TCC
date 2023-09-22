def freq_palavras(frases):
    dici={}
    frases=frases.split()
    for pal in frases:
        if pal not in dici:
            dici[pal]=frases.count(pal)
            
           
    return dici