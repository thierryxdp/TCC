def lingua_p(palv):
    palv_p=''
    for l in palv.lower():
        if l in 'aeiouáéíóúàèìòùâêîôûãõäëïöü':
            palv_p+=l+'p'+l
        else:
            palv_p+= l 
    return palv_p