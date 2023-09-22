def lingua_p(frase):
    """Função que recebe uma frase e retorna a mesma 
    traduzida para a língua do P. 
    str -> str"""
    frase = list(frase.lower())
    i = 0
    for x in frase:
        if x in 'ãaáeéiouú':
            concatenada = 'p'+x
            frase.insert(frase.index(x,i)+1,concatenada)
        i += 1
    copia = ''.join(frase)
    return copia