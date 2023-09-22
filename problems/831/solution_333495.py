def lingua_p(palv):
    palv_p=''
    for l in palavra.lower():
        if l in 'aeiou':
            palv_p+=l+'p'+l
        else:
            palv_p+= l 
    return palv_p