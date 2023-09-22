def uppCons(frase):
    indice = 0 
    frasenova = ''
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            frasenova = frasenova + str.upper(frase[indice])
        else:
            frasenova = frasenova + frase[indice]
        indice += 1    
    return frasenova