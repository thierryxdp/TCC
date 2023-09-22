def lingua_p(palavra):
    """recebe como parametro uma palavra e retorna traduzida para lingua do p"""
    p=''
    for letra in palavra :
        if letra in 'aeiouáéíóú':
            p=p+letra+'p'+letra
    return str.lower(p)