def uppCons(frase):
    """A função retorna todas as suas consoantes em maiúsculas e
    os demais caracteres exatamente como estavam na frase original.
    str-->str."""
    i = 0
    lista_frase = list(frase)
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    nova_lista =[]
    while i < len(lista_frase):
        if lista_frase[i] in consoantes:
            list.insert(nova_lista,i,lista_frase[i].upper())
            i += 1
        else:
            list.insert(nova_lista,i,lista_frase[i])
            i += 1
    return str.join('',nova_lista)