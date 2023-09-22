def uppcos(vivavida):
    i=0
    while i<len(vivavida):
        if vivavida[i] in 'bcdfghjklmnpqrstvxwz':
           str.upper(vivavida[i])
        i=i+1
    return vivavida