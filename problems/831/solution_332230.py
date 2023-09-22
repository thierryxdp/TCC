def lingua_p(frase):
    """Função recebe uma frase e retorna
    a mesma traduzida para a língua do P. 
    str -> str
    """
    frase = list(frase.lower())
    i = 0
    for x in frase:
        if x in 'ãaáeéiouú':
            c = 'p'+x
            frase.insert(frase.index(x,i)+1,c)
        i += 1
    copia = ''.join(frase)
    return copia