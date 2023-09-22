def lingua_p(palavra):
    """Função que recebe uma frase e retorna a mesma traduzida para a língua do P. str -> str"""
    palavra = list(palavra.lower())
    i = 0
    for vogal in palavra:
        if vogal in 'ãaáeéiouú':
            concatenada = 'p'+vogal
            palavra.insert(palavra.index(vogal,i)+1,concatenada)
        i += 1
    copia = ''.join(palavra)
    return copia