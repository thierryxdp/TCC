def lingua_p(palavra):
    """ Função que traduz a palavra para a língua do P
    str -> str """
    x='AEIOUaeiou'
    lista=[]
    for letra in palavra:
        if letra in x:
            lista=lista+[letra+'p'+letra]
        else:
            lista=lista+[letra]
    return str.lower(lista[0])