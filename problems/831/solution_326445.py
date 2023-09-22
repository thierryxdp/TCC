def lingua_p(palavra):  
    f=''
    for c in palavra:
        crc=c
        if str.lower(crc) in 'aeiouáéíóú':
            crc=crc+'p'+crc
        f=f+crc
    return f