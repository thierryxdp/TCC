def lingua_p(palavra):
    """Retorna a palavra, dada como entrada, traduzida para a língua do p
       str->str"""
    ubs = ''
    for a in palavra:
        if a in 'AEIOUaeiou':
            ubs = ubs + a + 'p'+ a
        else:
            ubs = ubs + a
    return ubs