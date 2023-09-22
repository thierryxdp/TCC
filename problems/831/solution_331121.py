def lingua_p(palavra):
    """Função que recebe uma palavra, transforma tudo
    para minúsculo e transforma ela pra uma palavra
    da lingua do p
    str -> str"""
    palavra = str.lower(palavra)
    p = ''
    for l in palavra:
        p = p + l
        if l in 'aeiou':
            p = p + 'p' + l
    return p