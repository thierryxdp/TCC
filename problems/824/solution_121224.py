def uppCons(frase):
    frasenova = ''
    for i in frase:
        if i in 'bcdfghjklmnpqrstvxwyzç':
            frasenova += i.upper() 
        else: 
            frasenova += i
    return frasenova