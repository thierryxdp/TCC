def uppCons(frase):
    proximo = 0
    lista = list(frase)
    frasenova = []
    while proximo < len(frase):
        if lista[proximo] not in 'AEIOUaeiou':
            list.append(frasenova,str.upper(lista[proximo]))
        else:
            list.append(frasenova,lista[proximo])
        proximo = proximo + 1
    return str.join('',frasenova)