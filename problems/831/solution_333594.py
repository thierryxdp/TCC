def lingua_p(palv):
    palv_p=''
    vog='aeiouáéíóúàèìòùâêîôûãõäëïöü'
    l=0
    while l<=len(palv.lower()):
        if palv[l] in vog:
            palv_p+=palv[l]+'p'+palv[l]
        else:
            palv_p+=palv[l] 
        l+=1
    return palv_p