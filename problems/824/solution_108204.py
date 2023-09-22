def uppCons(frase):
    i=0
    lisfrase = frase.split(' ')
    lista = []
    while i<len(frase):
        if lisfrase[i] in 'AEIOUaeiou':
            lista = lisfrase[i]
        else:
            lista = lisfrase[i].upper
            
    return str(lista)