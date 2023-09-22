def lingua_p(palavra):
    i = 0
    lista = list(palavra)
    retorno = []
    for c in lista:
        if c in ('a','e','i','o','u'):
            retorno.insert(i,c + 'p' + c)
        else:
            retorno.insert(i,c)
        i += 1
    return str.lower(str.join('',retorno))