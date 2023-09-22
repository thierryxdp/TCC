def lingua_p(palavra):
    """ """
    proximo = 0
    lista = ['a','a','a','e','e','i','o','u']
    for i in palavra:
        if lista[proximo] in palavra:
            proximo = proximo + 1
            retorno = str.join('p'+lista[proximo],(str.replace(palavra,lista[proximo],'',1)))
    return  retorno