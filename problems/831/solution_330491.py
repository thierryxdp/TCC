def lingua_p (palavra):
    """a função recebe uma palavra em português e transforma para a lingua p, adicionando um p + vo
    gal após cada vogal da palavra orignal. A vogal adicionada sera igual a vogal antes do p.
    str -> str"""
    string = ''
    str.lower (palavra)
    for x in palavra:
        if x in 'aeiou':
            x = x + 'p' + x
    	string = string + x
    return string