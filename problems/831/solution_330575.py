def lingua_p(palavra):
    """..."""
    mini = str.lower(palavra)
    traducao = ''
    for i in palavra:
        if i in 'aeiouáâãéêóôú':
            traducao = traducao + i + 'p' + i
        elif i in 'bcdfghjklmnpqrstvwxyzç':
            traducao = traducao + i
    return traducao