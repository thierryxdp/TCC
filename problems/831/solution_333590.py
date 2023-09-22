def lingua_p(palv):
    palv_p=''
    l=0
    while l<=len(palv.lower()):
        if palv[l] in 'aeiouáéíóúàèìòùâêîôûãõäëïöü':
            palv_p+=palv[l]+'p'+palv[l]
        else:
            palv_p+=palv[l] 
    return palv_p