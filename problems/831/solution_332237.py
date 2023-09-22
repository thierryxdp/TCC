def lingua_p(palavra):
    """Função que recebe uma frase e retorna a mesma traduzida para a língua do P. str -> str"""
    palavra = list(palavra.lower())
    i = 0
    for x in palavra:
        if x in 'ãaáeéiouú':
            concatenada = 'p'+x
            palavra.insert(frase.index(x,i)+1,concatenada)
        i += 1
    copia = ''.join(frase)
    return copia