def freq_palavras(frases):
    palv_p=''
    vog='aeiouáéíóúàèìòùâêîôûãõäëïöü'
    l=0
    while l<len(frases.lower()):
        if frases.lower[l] in vog:
            palv_p+=frases[l]+'p'+frases[l]
        else:
            palv_p+=frases[l] 
        l+=1
    return palv_p