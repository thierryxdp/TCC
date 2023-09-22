#str -> str
def lingua_p(palv):
    #definir variável para a palv traduzida para a língua do p
    palv_p=''
    #realizar o processo de tradução
    for l in palv.lower():
        if l in 'aeiouáéíóúàèìòùâêîôûãõäëïöü':
            palv_p+=l+'p'+l
        else:
            palv_p+= l 
    return palv_p