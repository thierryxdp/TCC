def lingua_p(palavra):
    '''Transforma uma palavra da língua portuguesa
    para a língua do P;
    str -> str'''
    
    palavra = palavra.lower()
    acumulador = str()
    for letra in palavra:
        if letra not in 'bcdfghjklmnpqrstuvwxyzç':
        	acumulador += letra + 'p' + letra
        else:
            acumulador += letra
    return acumulador