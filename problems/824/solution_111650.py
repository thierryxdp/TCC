def uppCons(frase):
    '''deixa todas as consoantes em maiusculo
	str -> str'''
    proximo = 0
    lista = list(frase)
    frasenova = []
    while proximo < len(frase):
        if lista[proximo] not in 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕãõ':
            list.append(frasenova,str.upper(lista[proximo]))
        else:
            list.append(frasenova,lista[proximo])
        proximo = proximo + 1
    return str.join('',frasenova)