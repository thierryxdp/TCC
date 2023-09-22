def lingua_p(palavra):
    """ """
    proximo = 0
    lista = ['a','e','i','o','u']
    for i in palavra:
        if lista[proximo] in palavra:
            proximo = proximo + 1
            retorno = str.join(lista[proximo]+'p',(str.replace(palavra,proximo,''))
    return  retorno