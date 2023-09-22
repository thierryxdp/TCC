def uppCons(frase):
    retorno = []
    x=0
    while x < len(frase):
        if frase[x] in ['a','e','i','o','u']:
            retorno.append(frase[x])
        else:
            retorno.append(frase[x].upper())
    retorno = ''.join(retorno)