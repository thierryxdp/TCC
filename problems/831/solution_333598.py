def lingua_p(palv):
    palv_p=''
    vog='aeiouáéíóúàèìòùâêîôûãõäëïöü'
    l=0
    while l<=len(palv.lower()):
        if palv.lower[l] in vog:
            palv_p+=palv.lower()[l]+'p'+palv.lower()[l]
        else:
            palv_p+=palv.lower()[l] 
        l+=1
    return palv_p