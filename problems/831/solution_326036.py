def lingua_p(palavra):
    ''' Converte a palavra recebida para a lingua do P. str->str'''
    f=''
    for c in palavra:
        crc=c
        if str.lower(crc) in 'aeiouáéíóú':
            crc=crc+'p'+crc
        f=f+crc
    return f