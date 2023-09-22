def lingua_p (palavra):
    '''Dada uma palavra, retorne ela traduzida para a
       língua do P;
       string -> string'''
    i = 0
    for letra in palavra:
        if letra in 'qwrtypsdfghjklçzxcvbnm':
            palavra = palavra[:i+1]+'p'+letra+palavra[i+1:]
            i = i+3
        else:
            i = i+1
        palavra = palavra.lower()
    return palavra