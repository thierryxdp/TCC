def lingua_p(palavra):
    """ """
    proximo = 0
    lista = ['a','e','i','o','u']
    for i in palavra:
        if lista[proximo] in palavra:
            proximo = proximo + 1
            retorno = str.join(lista[proximo-1]+'p',(str.replace(palavra,lista[proximo-1],'',1)))
    return  retorno