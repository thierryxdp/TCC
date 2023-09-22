def auxilio(frase):
    
    
    str.split(frase)
    vogal = ['a', 'e', 'i', 'o', 'u']
    i = 0
    
    for i in frase:
        if i not in vogal:
            str.upper(i)
    return frase    

def uppCons(frase):
    
    lista = str.join('', map(auxilio, frase))
    
    return lista