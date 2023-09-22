def lingua_p(palavra):
    """  """
    nova=''
    for letra in palavra:
        if letra.lower() in 'aeiouáéíóú':
            nova=nova+letra+'p'+letra
        else:
            nova=nova+letra
    return nova.lower()