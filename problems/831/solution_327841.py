def lingua_p(frase):
    ultimo = None
    for atual in frase:
        if atual == ultimo:
            yield 'p'
        yield atual
    ultimo = atual
    print(''.join(lingua_p(s)))