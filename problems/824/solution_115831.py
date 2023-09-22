def maiusculas(texto):
    lista=list(texto)
    i=0
    nova=[]
    while i<len(lista):
        if lista[i]not in 'AEIOUaeiou':
            nova=nova+list(str.upper(texto[i]))
            i=i+1
        else:
            nova = nova + list(texto[i])
            i=i+1
    return str.join('',nova)