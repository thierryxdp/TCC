def lingua_p(palavra):
    lista=[]
    p=list(palavra)
    for letra in p:
        if letra in 'aeiouáéíóú':
            lista=letra+'p'+letra
        else:
            lista=lista+letra
    return str.join(lista,' ')