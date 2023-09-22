def lingua_p():
    """  """
    nova=''
    for letra in nova:
        if letra.lower90 in 'aeiouáú':
            nova=nova+letra+'p'+letra
        else:
            nova+nova+letra
    return nova.lower()