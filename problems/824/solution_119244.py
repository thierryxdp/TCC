#a funcao retorna as consoantes em letra maiuscula 
def uppCons (x):
    y = ""
    for z in x:
        if z in 'bcdfghjklmnpqrstvwxyzç':
            y += str.upper(z)
        else:
            y += z
    return y