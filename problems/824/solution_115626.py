def uppCons(frase):
    m = 0
    lista = list(frase)
   
    while m < len(lista):
        letra = lista[m]
        if lista[m] in 'AEIOUáéíóúÁÉÍÓÚaeiouãõÃÕ':
            m = m + 1
        else:
            lista[m] = letra.upper()
            m = m + 1

    return ''.join(lista)