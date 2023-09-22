def freq_palaresa(frases):
    dici={}
    frases=frases.loer()
    frases=frase.split()
    for pal in frases:
        if pal not in dici:
            dici[pal]=pal.count(frases):
    return dici