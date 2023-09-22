def lingua_p(palavra):
    'dado uma palavra retorne esta mesma palavra na lingua do p.str-->str'
    palavrap=''
    for l in palavra:
        if l in 'aeiouáéíóú':
            palavrap=palavrap+l+'p'+l
        else:
            palavrap=palavrap+l
    return palavrap