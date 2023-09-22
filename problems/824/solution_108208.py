def uppCons(frase):
    i=0
    lista = ''
    while i<len(frase):
        if frase[i] in 'AEIOUaeiou':
            lista = lista + frase[i]
        else:
            lista = lista + lisfrase[i].upper
        i=i+1
            
    return lista