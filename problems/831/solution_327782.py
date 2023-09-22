def lingua_p(palavra):
    """ Dado uma string palavra, retorna ela na lingua do P,
    que consiste na mesma palavra porém com um p antes e depois de cada vogal.
    string -> string
    """
    resultado = ''
    for i in palavra:
        if i.lower() in 'aeiou':
            resultado += i + 'p' + i
        else:
            resultado += i
    return resultado