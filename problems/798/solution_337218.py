def freq_palavras(frases):
    dici={}
    frases=frases.lower()
    frases=frases.split()
    for pal in frases:
        if pal not in dici:
            dici[frases]=pal.count(pal)
            
           
    return dici