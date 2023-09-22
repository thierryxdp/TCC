def lingua_p(palavra):
    """ddsfmndsj"""
    palavra = palavra.lower()
    
    for x in palavra:
        if x in 'aãaéiou':
            soma = 'p'+x
            palavra.insert((palavra[x]+1), soma)
    copia = ''.join(palavra)
    return copia