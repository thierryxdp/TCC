def freq_palavras(frases):
    dici={}
    frases=frases.lower()
    frases=frase.split()
    for pal in frases:
        if pal not in dici:
            dici[pal]=pal.count(pal)
            
           
    return dici